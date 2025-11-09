from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List, Optional
import io
import csv

from ..db import get_db
from ..models import db_models, pydantic_models

router = APIRouter(
    prefix="/api",
    tags=["Sites"]
)

# --- 1. GET /api/sites ---
@router.get("/sites", response_model=List[pydantic_models.SiteWithScoreSchema])
def get_all_sites(
    min_score: Optional[float] = Query(None, ge=0, le=100),
    max_score: Optional[float] = Query(None, ge=0, le=100),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """
    Returns all sites from the `sites_with_scores` view, with filters
    and pagination. Sorted by score descending by default.
    """
    query = db.query(db_models.SiteWithScore)
    
    if min_score is not None:
        query = query.filter(db_models.SiteWithScore.total_suitability_score >= min_score)
    
    if max_score is not None:
        query = query.filter(db_models.SiteWithScore.total_suitability_score <= max_score)
        
    # --- FIX for mysql-connector ---
    # The .nulls_last() function is not compatible with the mysql-connector driver
    # We use this alternative method to sort NULLs to the bottom.
    query = query.order_by(
        db_models.SiteWithScore.total_suitability_score.is_(None),
        db_models.SiteWithScore.total_suitability_score.desc()
    )
    
    # Apply pagination
    query = query.limit(limit).offset(offset)
    
    sites = query.all()
    
    # Convert SQLAlchemy models to Pydantic models (Decimal to float)
    result = [pydantic_models.SiteWithScoreSchema.model_validate(site) for site in sites]
    
    return result

# --- 2. GET /api/sites/{id} --- (UPDATED SECTION)
@router.get("/sites/{id}", response_model=pydantic_models.SiteDetailResponse)
def get_site_by_id(id: int, db: Session = Depends(get_db)):
    """
    Returns detailed information for a specific site from the
    `sites_with_scores` view.
    """
    site = db.query(db_models.SiteWithScore).filter(db_models.SiteWithScore.site_id == id).first()
    
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
        
    return pydantic_models.SiteDetailResponse.model_validate(site)

# --- 3. POST /api/analyze ---
@router.post("/analyze", response_model=dict)
def trigger_analysis_with_custom_weights(
    request_body: pydantic_models.WeightsRequest,
    db: Session = Depends(get_db)
):
    """
    Triggers a recalculation with custom weights.
    This updates the `analysis_parameters` table and
    calls the `calculate_suitability_scores` stored procedure.
    """
    # request_body.weights.model_dump(by_alias=True) will convert
    # Pydantic model (e.g., "solar") to the alias (e.g., "solar_irradiance_weight")
    weights = request_body.weights.model_dump(by_alias=True)
    
    try:
        # Update each weight in the database
        for param_name, weight_value in weights.items():
            db.execute(
                text("UPDATE analysis_parameters SET weight_value = :value WHERE parameter_name = :name"),
                {"value": weight_value, "name": param_name}
            )
        
        # Call the stored procedure to recalculate all scores
        # Note: We must call this AFTER updating the weights
        db.execute(text("CALL calculate_suitability_scores()"))
        
        db.commit()
        
        return {"message": "Analysis recalculated successfully with new weights."}
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


# --- 4. GET /api/statistics ---
@router.get("/statistics", response_model=pydantic_models.StatisticsResponse)
def get_summary_statistics(db: Session = Depends(get_db)):
    """
    Returns summary statistics across all sites from the
    `sites_with_scores` view.
    """
    query = text("""
        SELECT 
            COUNT(*) as total_sites,
            AVG(total_suitability_score) as avg_score,
            MIN(total_suitability_score) as min_score,
            MAX(total_suitability_score) as max_score,
            STDDEV(total_suitability_score) as std_dev
        FROM sites_with_scores
        WHERE total_suitability_score IS NOT NULL;
    """)
    
    result = db.execute(query).first()
    
    if not result or result[0] == 0:
        # Return default values if no sites are found
        return pydantic_models.StatisticsResponse(
            total_sites=0,
            avg_score=None,
            min_score=None,
            max_score=None,
            std_dev=None
        )
        
    # Manually map to Pydantic model
    return pydantic_models.StatisticsResponse(
        total_sites=result[0],
        avg_score=result[1],
        min_score=result[2],
        max_score=result[3],
        std_dev=result[4]
    )

# --- 5. GET /api/export ---
@router.get("/export")
def export_results(
    format: str = Query("json", enum=["json", "csv"]),
    min_score: Optional[float] = Query(None, ge=0, le=100),
    max_score: Optional[float] = Query(None, ge=0, le=100),
    db: Session = Depends(get_db)
):
    """
    Exports filtered results as CSV or JSON.
    """
    # Get filtered site data (re-using logic from /sites)
    query = db.query(db_models.SiteWithScore)
    if min_score is not None:
        query = query.filter(db_models.SiteWithScore.total_suitability_score >= min_score)
    if max_score is not None:
        query = query.filter(db_models.SiteWithScore.total_suitability_score <= max_score)

    # --- FIX for mysql-connector ---
    query = query.order_by(
        db_models.SiteWithScore.total_suitability_score.is_(None),
        db_models.SiteWithScore.total_suitability_score.desc()
    )
    sites = query.all()

    # Convert to Pydantic models to handle Decimal, etc.
    sites_data = [pydantic_models.SiteWithScoreSchema.model_validate(site).model_dump() for site in sites]

    if format == "json":
        return sites_data

    if format == "csv":
        output = io.StringIO()
        if not sites_data:
            # Handle empty case
            output.write("No data found.\n")
            return StreamingResponse(iter([output.getvalue()]), media_type="text/csv")

        # Use keys from the first item as header
        writer = csv.DictWriter(output, fieldnames=sites_data[0].keys())
        writer.writeheader()
        writer.writerows(sites_data)
        
        return StreamingResponse(
            iter([output.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=solar_site_export.csv"}
        )