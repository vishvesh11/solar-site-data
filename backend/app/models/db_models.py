from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, JSON, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db import Base

# orm modles for Db using Sql alchemy


class Site(Base):
    __tablename__ = "sites"
    
    site_id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String(255), nullable=False)
    latitude = Column(Numeric(10, 7), nullable=False)
    longitude = Column(Numeric(10, 7), nullable=False)
    area_sqm = Column(Integer, nullable=False)
    solar_irradiance_kwh = Column(Numeric(4, 2), nullable=False)
    grid_distance_km = Column(Numeric(5, 2), nullable=False)
    slope_degrees = Column(Numeric(4, 2), nullable=False)
    road_distance_km = Column(Numeric(5, 2), nullable=False)
    elevation_m = Column(Integer, nullable=False)
    land_type = Column(String(50), nullable=False)
    region = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationship to analysis_results
    results = relationship("AnalysisResult", back_populates="site")

class AnalysisParameter(Base):
    __tablename__ = "analysis_parameters"
    
    param_id = Column(Integer, primary_key=True, index=True)
    parameter_name = Column(String(100), nullable=False, unique=True)
    weight_value = Column(Numeric(4, 3), nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    
    result_id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey("sites.site_id", ondelete="CASCADE"), nullable=False)
    solar_irradiance_score = Column(Numeric(5, 2), nullable=False)
    area_score = Column(Numeric(5, 2), nullable=False)
    grid_distance_score = Column(Numeric(5, 2), nullable=False)
    slope_score = Column(Numeric(5, 2), nullable=False)
    infrastructure_score = Column(Numeric(5, 2), nullable=False)
    total_suitability_score = Column(Numeric(5, 2), nullable=False, index=True)
    analysis_timestamp = Column(DateTime, server_default=func.now())
    parameters_snapshot = Column(JSON)
    

    site = relationship("Site", back_populates="results")


class SiteWithScore(Base):
    __tablename__ = "sites_with_scores"
    
    site_id = Column(Integer, primary_key=True) 
    site_name = Column(String(255))
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
    area_sqm = Column(Integer)
    solar_irradiance_kwh = Column(Numeric(4, 2))
    grid_distance_km = Column(Numeric(5, 2))
    slope_degrees = Column(Numeric(4, 2))
    road_distance_km = Column(Numeric(5, 2))
    elevation_m = Column(Integer)
    land_type = Column(String(50))
    region = Column(String(100))
    solar_irradiance_score = Column(Numeric(5, 2))
    area_score = Column(Numeric(5, 2))
    grid_distance_score = Column(Numeric(5, 2))
    slope_score = Column(Numeric(5, 2))
    infrastructure_score = Column(Numeric(5, 2))
    total_suitability_score = Column(Numeric(5, 2))
    analysis_timestamp = Column(DateTime)