
# Calculations for solar irridiance
def calculate_solar_score(solar_irradiance_kwh: float) -> float:
    """
    Args:
        solar_irradiance_kwh: Average daily solar irradiance (kWh/m²/day)
    Returns:
        Score between 0-100
    """
    if solar_irradiance_kwh >= 5.5:
        return 100.0
    elif solar_irradiance_kwh < 3.0:
        return 0.0
    else:
        # Linear interpolation between 3.0 and 5.5
        return ((solar_irradiance_kwh - 3.0) / 2.5) * 100

# calculation for Area
def calculate_area_score(area_sqm: float) -> float:
    """
    Args:
        area_sqm: Available area in square meters
    Returns:
        Score between 0-100
    """
    if area_sqm >= 50000:
        return 100.0
    elif area_sqm < 5000:
        return 0.0
    else:
        return ((area_sqm - 5000) / 45000) * 100

# GriD Distance score
def calculate_grid_score(grid_distance_km: float) -> float:
    """
    Args:
        grid_distance_km: Distance to nearest power grid (km)
    Returns:
        Score between 0-100
    """
    if grid_distance_km <= 1:
        return 100.0
    elif grid_distance_km >= 20:
        return 0.0
    else:
        return 100 - ((grid_distance_km - 1) / 19) * 100

# Calculation for Slope score
def calculate_slope_score(slope_degrees: float) -> float:
    """
    Args:
        slope_degrees: Terrain slope in degrees (0 = flat)
    Returns:
        Score between 0-100
    """
    if slope_degrees <= 5:
        return 100.0
    elif slope_degrees > 20:
        return 0.0
    elif slope_degrees <= 15:
        # First tier: 5-15 degrees
        return 100 - ((slope_degrees - 5) / 10) * 50
    else:
        # Second tier: 15-20 degrees
        return 50 - ((slope_degrees - 15) / 5) * 50

# calculation for Infrastructure score
def calculate_infrastructure_score(road_distance_km: float) -> float:
    """
    Args:
        road_distance_km: Distance to nearest road (km)
    Returns:
        Score between 0-100
    """
    if road_distance_km <= 0.5:
        return 100.0
    elif road_distance_km >= 5:
        return 0.0
    else:
        return 100 - ((road_distance_km - 0.5) / 4.5) * 100

def validate_weights(weights_dict: dict) -> bool:
    """
    Validates that weights sum to 1.0.
    """
    total = sum(weights_dict.values())
    if abs(total - 1.0) > 0.001:
        raise ValueError(f"Weights must sum to 1.0, got {total}")
    
    for key, value in weights_dict.items():
        if not (0 <= value <= 1):
            raise ValueError(f"Weight {key} must be between 0 and 1, got {value}")
    
    return True


class SuitabilityCalculator:
    """
    Python-side calculator class to bundle scoring logic.
    """
    def __init__(self, weights: dict = None):
        self.weights = weights or {
            'solar': 0.35,
            'area': 0.25,
            'grid': 0.20,
            'slope': 0.15,
            'infrastructure': 0.05
        }
        validate_weights(self.weights)
    
    def calculate(self, site_data: dict) -> (float, dict):
        """
        Calculates the total score and individual score breakdown.
        
        Args:
            site_data: A dict with keys:
                'solar_irradiance_kwh', 'area_sqm', 'grid_distance_km',
                'slope_degrees', 'road_distance_km'
        
        Returns:
            A tuple of (total_score, scores_breakdown)
        """
        scores = {
            'solar': calculate_solar_score(site_data['solar_irradiance_kwh']),
            'area': calculate_area_score(site_data['area_sqm']),
            'grid': calculate_grid_score(site_data['grid_distance_km']),
            'slope': calculate_slope_score(site_data['slope_degrees']),
            'infrastructure': calculate_infrastructure_score(site_data['road_distance_km'])
        }
        
        total = sum(
            scores[key] * self.weights[key] 
            for key in scores.keys()
        )
        
        return round(total, 2), scores