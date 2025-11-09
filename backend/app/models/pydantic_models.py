from pydantic import BaseModel, Field, model_validator
from typing import List, Optional, Dict
from datetime import datetime



# api modles using Pydantic

class SiteWithScoreSchema(BaseModel):
    """
    Response model for a single site, based on the `sites_with_scores` view.
    """
    site_id: int
    site_name: str
    latitude: float
    longitude: float
    area_sqm: int
    solar_irradiance_kwh: float
    grid_distance_km: float
    slope_degrees: float
    road_distance_km: float
    elevation_m: int
    land_type: str
    region: str
    
    # Analysis Results
    solar_irradiance_score: Optional[float] = None
    area_score: Optional[float] = None
    grid_distance_score: Optional[float] = None
    slope_score: Optional[float] = None
    infrastructure_score: Optional[float] = None
    total_suitability_score: Optional[float] = None
    analysis_timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True 

class StatisticsResponse(BaseModel):
    """
    Response model for the /api/statistics endpoint.
    """
    total_sites: int
    avg_score: Optional[float] = None
    min_score: Optional[float] = None
    max_score: Optional[float] = None
    std_dev: Optional[float] = None

# --- NEW SCHEMA ---
class SiteDetailResponse(SiteWithScoreSchema):

    #Response model for the GET /api/sites/{id} endpoint.
    #alias for SiteWithScoreSchema.

    pass


# --- Request Schemas ---

class Weights(BaseModel):
   
    solar: float = Field(..., ge=0, le=1, alias='solar_irradiance_weight')
    area: float = Field(..., ge=0, le=1, alias='area_weight')
    grid: float = Field(..., ge=0, le=1, alias='grid_distance_weight')
    slope: float = Field(..., ge=0, le=1, alias='slope_weight')
    infrastructure: float = Field(..., ge=0, le=1, alias='infrastructure_weight')
    
    class Config:
        populate_by_name = True 

    @model_validator(mode='after')
    def validate_weights_sum(self) -> 'Weights':
        # validates the weight if it is 1.00
        total = self.solar + self.area + self.grid + self.slope + self.infrastructure
        if abs(total - 1.0) > 0.001:
            raise ValueError(f"weights must sum to 1.0, but is {total}")
        return self
    
# Request body for the POST /api/analyze endpoint.
class WeightsRequest(BaseModel):

    
    weights: Weights