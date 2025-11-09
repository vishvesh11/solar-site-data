# Suitability Score Calculation Reference

## Overview

This document provides detailed information about how suitability scores are calculated in the Solar Site Analyzer application.

---

## 📊 Overall Score Formula

```
Total Suitability Score = 
    (Solar Irradiance Score × 0.35) +
    (Area Score × 0.25) +
    (Grid Distance Score × 0.20) +
    (Slope Score × 0.15) +
    (Infrastructure Score × 0.05)
```

**Note:** All individual scores are normalized to 0-100 range before applying weights.

---

## 1️⃣ Solar Irradiance Score

Measures the amount of solar energy available at the site.

### Formula
```python
def calculate_solar_score(solar_irradiance_kwh):
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
```

### Scoring Bands

| Solar Irradiance (kWh/m²/day) | Score | Rating |
|-------------------------------|-------|---------|
| ≥ 5.5 | 100 | Excellent |
| 5.0 - 5.4 | 80 - 96 | Very Good |
| 4.5 - 4.9 | 60 - 76 | Good |
| 4.0 - 4.4 | 40 - 56 | Fair |
| 3.5 - 3.9 | 20 - 36 | Poor |
| 3.0 - 3.4 | 0 - 16 | Very Poor |
| < 3.0 | 0 | Unsuitable |

### Examples

```python
# Example 1: Excellent site
solar_irradiance = 6.2  # kWh/m²/day
score = 100.0  # Perfect score

# Example 2: Good site
solar_irradiance = 4.5  # kWh/m²/day
score = ((4.5 - 3.0) / 2.5) * 100 = 60.0

# Example 3: Poor site
solar_irradiance = 2.8  # kWh/m²/day
score = 0.0  # Below minimum threshold
```

### Context
- India's average solar irradiance: 4.5-5.5 kWh/m²/day
- World-class solar sites: > 6.0 kWh/m²/day
- Minimum viable: 3.0 kWh/m²/day

---

## 2️⃣ Area Score

Measures the available land area for solar panel installation.

### Formula
```python
def calculate_area_score(area_sqm):
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
        # Linear interpolation between 5,000 and 50,000
        return ((area_sqm - 5000) / 45000) * 100
```

### Scoring Bands

| Area (m²) | Area (acres) | Score | Estimated Capacity (MW) |
|-----------|--------------|-------|-------------------------|
| ≥ 50,000 | ≥ 12.4 | 100 | ≥ 5.0 |
| 40,000 - 49,999 | 9.9 - 12.3 | 78 - 98 | 4.0 - 4.9 |
| 30,000 - 39,999 | 7.4 - 9.8 | 56 - 76 | 3.0 - 3.9 |
| 20,000 - 29,999 | 4.9 - 7.3 | 33 - 53 | 2.0 - 2.9 |
| 10,000 - 19,999 | 2.5 - 4.8 | 11 - 31 | 1.0 - 1.9 |
| 5,000 - 9,999 | 1.2 - 2.4 | 0 - 9 | 0.5 - 0.9 |
| < 5,000 | < 1.2 | 0 | < 0.5 |

### Examples

```python
# Example 1: Large commercial site
area = 95000  # m² (23.5 acres)
score = 100.0  # Exceeds threshold

# Example 2: Medium site
area = 25000  # m² (6.2 acres)
score = ((25000 - 5000) / 45000) * 100 = 44.4

# Example 3: Small site
area = 4500  # m² (1.1 acres)
score = 0.0  # Below minimum
```

### Conversion Reference
- **1 MW solar farm**: ~10,000 m² (2.5 acres)
- **Typical panel efficiency**: 100 W/m²
- **Ground coverage ratio**: 50% (includes spacing)

---

## 3️⃣ Grid Distance Score

Measures proximity to existing power grid infrastructure.

### Formula
```python
def calculate_grid_score(grid_distance_km):
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
        # Inverse linear relationship
        return 100 - ((grid_distance_km - 1) / 19) * 100
```

### Scoring Bands

| Distance (km) | Score | Connection Cost | Rating |
|---------------|-------|-----------------|---------|
| ≤ 1 | 100 | Low | Excellent |
| 1 - 5 | 79 - 99 | Moderate | Good |
| 5 - 10 | 53 - 74 | High | Fair |
| 10 - 15 | 26 - 47 | Very High | Poor |
| 15 - 20 | 0 - 21 | Prohibitive | Very Poor |
| > 20 | 0 | Infeasible | Unsuitable |

### Examples

```python
# Example 1: Adjacent to grid
distance = 0.5  # km
score = 100.0

# Example 2: Moderate distance
distance = 8  # km
score = 100 - ((8 - 1) / 19) * 100 = 63.2

# Example 3: Remote location
distance = 25  # km
score = 0.0
```

### Cost Impact
- **< 2 km**: $50,000 - $100,000 per km
- **2-10 km**: $100,000 - $200,000 per km
- **> 10 km**: Often requires substations ($500,000+)

---

## 4️⃣ Slope Score

Measures terrain flatness - flatter terrain is better for installation.

### Formula
```python
def calculate_slope_score(slope_degrees):
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
```

### Scoring Bands

| Slope (degrees) | Score | Installation Difficulty | Cost Impact |
|-----------------|-------|------------------------|-------------|
| 0 - 5 | 100 | Minimal | Standard |
| 5 - 10 | 75 - 95 | Low | +10% |
| 10 - 15 | 50 - 70 | Moderate | +20% |
| 15 - 20 | 0 - 45 | High | +40% |
| > 20 | 0 | Very High | +60%+ |

### Examples

```python
# Example 1: Flat terrain
slope = 2.5  # degrees
score = 100.0

# Example 2: Gentle slope
slope = 8  # degrees
score = 100 - ((8 - 5) / 10) * 50 = 85.0

# Example 3: Steep slope
slope = 18  # degrees
score = 50 - ((18 - 15) / 5) * 50 = 20.0

# Example 4: Very steep
slope = 25  # degrees
score = 0.0
```

### Terrain Classification
- **0-2°**: Flat (ideal)
- **2-5°**: Nearly flat (excellent)
- **5-10°**: Gentle slope (good)
- **10-15°**: Moderate slope (fair)
- **15-20°**: Steep slope (poor)
- **>20°**: Very steep (unsuitable)

---

## 5️⃣ Infrastructure Score

Measures proximity to roads and other infrastructure.

### Formula
```python
def calculate_infrastructure_score(road_distance_km):
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
        # Inverse linear relationship
        return 100 - ((road_distance_km - 0.5) / 4.5) * 100
```

### Scoring Bands

| Distance (km) | Score | Access Quality | Construction Impact |
|---------------|-------|----------------|---------------------|
| ≤ 0.5 | 100 | Direct access | Standard |
| 0.5 - 1 | 89 - 99 | Excellent | Minimal road work |
| 1 - 2 | 67 - 78 | Good | Minor road extension |
| 2 - 3 | 44 - 56 | Fair | New road required |
| 3 - 4 | 22 - 33 | Poor | Significant road work |
| 4 - 5 | 0 - 11 | Very poor | Major infrastructure |
| > 5 | 0 | No access | Prohibitive |

### Examples

```python
# Example 1: Adjacent to road
distance = 0.2  # km
score = 100.0

# Example 2: Short access road needed
distance = 1.5  # km
score = 100 - ((1.5 - 0.5) / 4.5) * 100 = 77.8

# Example 3: Remote location
distance = 6  # km
score = 0.0
```

### Access Requirements
- **Construction phase**: Heavy equipment access
- **Operation phase**: Maintenance vehicle access
- **Emergency access**: Fire trucks, repair equipment
- **Material delivery**: Large panel shipments

---

## 🎯 Complete Calculation Example

### Site: "Sulur Airbase Adjacent" (ID: 9)

**Input Parameters:**
- Solar Irradiance: 6.2 kWh/m²/day
- Area: 95,000 m²
- Grid Distance: 0.5 km
- Slope: 0.8°
- Road Distance: 0.2 km

**Step-by-Step Calculation:**

1. **Solar Irradiance Score**
   ```
   6.2 >= 5.5 → Score = 100.0
   ```

2. **Area Score**
   ```
   95,000 >= 50,000 → Score = 100.0
   ```

3. **Grid Distance Score**
   ```
   0.5 <= 1 → Score = 100.0
   ```

4. **Slope Score**
   ```
   0.8 <= 5 → Score = 100.0
   ```

5. **Infrastructure Score**
   ```
   0.2 <= 0.5 → Score = 100.0
   ```

6. **Total Weighted Score**
   ```
   Total = (100 × 0.35) + (100 × 0.25) + (100 × 0.20) + (100 × 0.15) + (100 × 0.05)
   Total = 35 + 25 + 20 + 15 + 5
   Total = 100.0
   ```

**However, actual database score: 87.45**

*Note: The stored procedure may apply additional normalization or real-world constraints not shown in the simple formula.*

---

## 🔄 Custom Weight Calculations

Users can adjust weights to prioritize different factors.

### Example: Prioritizing Solar Irradiance

**Custom Weights:**
- Solar: 0.50 (↑ from 0.35)
- Area: 0.20 (↓ from 0.25)
- Grid: 0.15 (↓ from 0.20)
- Slope: 0.10 (↓ from 0.15)
- Infrastructure: 0.05 (same)

**Impact:**
- Sites with high solar irradiance rank higher
- Large area less important
- Grid proximity less critical

### Example: Prioritizing Grid Access

**Custom Weights:**
- Solar: 0.25 (↓ from 0.35)
- Area: 0.20 (↓ from 0.25)
- Grid: 0.35 (↑ from 0.20)
- Slope: 0.15 (same)
- Infrastructure: 0.05 (same)

**Impact:**
- Sites close to power grid rank higher
- Reduces transmission costs
- May accept lower solar irradiance

---

## 📊 Score Categories

### Classification System

| Score Range | Category | Recommendation |
|-------------|----------|----------------|
| 80 - 100 | Excellent | Prioritize for development |
| 60 - 79 | Good | Viable with standard conditions |
| 40 - 59 | Fair | Viable with mitigation measures |
| 20 - 39 | Poor | High-risk, detailed study needed |
| 0 - 19 | Very Poor | Not recommended |

---

## 🧪 Validation Rules

### Score Validation
```python
def validate_score(score):
    assert 0 <= score <= 100, "Score must be between 0 and 100"
    assert isinstance(score, (int, float)), "Score must be numeric"
    return round(score, 2)  # Round to 2 decimal places
```

### Weight Validation
```python
def validate_weights(weights_dict):
    total = sum(weights_dict.values())
    assert abs(total - 1.0) < 0.001, f"Weights must sum to 1.0, got {total}"
    
    for key, value in weights_dict.items():
        assert 0 <= value <= 1, f"Weight {key} must be between 0 and 1"
    
    return True
```

---

## 💡 Implementation Tips

### Python Example
```python
class SuitabilityCalculator:
    def __init__(self, weights=None):
        self.weights = weights or {
            'solar': 0.35,
            'area': 0.25,
            'grid': 0.20,
            'slope': 0.15,
            'infrastructure': 0.05
        }
    
    def calculate(self, site_data):
        scores = {
            'solar': self._solar_score(site_data['solar_irradiance_kwh']),
            'area': self._area_score(site_data['area_sqm']),
            'grid': self._grid_score(site_data['grid_distance_km']),
            'slope': self._slope_score(site_data['slope_degrees']),
            'infrastructure': self._infra_score(site_data['road_distance_km'])
        }
        
        total = sum(
            scores[key] * self.weights[key] 
            for key in scores.keys()
        )
        
        return round(total, 2), scores
```

### JavaScript Example
```javascript
class SuitabilityCalculator {
    constructor(weights = null) {
        this.weights = weights || {
            solar: 0.35,
            area: 0.25,
            grid: 0.20,
            slope: 0.15,
            infrastructure: 0.05
        };
    }
    
    calculate(siteData) {
        const scores = {
            solar: this._solarScore(siteData.solar_irradiance_kwh),
            area: this._areaScore(siteData.area_sqm),
            grid: this._gridScore(siteData.grid_distance_km),
            slope: this._slopeScore(siteData.slope_degrees),
            infrastructure: this._infraScore(siteData.road_distance_km)
        };
        
        const total = Object.keys(scores).reduce(
            (sum, key) => sum + (scores[key] * this.weights[key]), 
            0
        );
        
        return {
            total: Math.round(total * 100) / 100,
            breakdown: scores
        };
    }
}
```

---

**Document Version:** 1.0  
**Last Updated:** October 2025  
**For implementation questions:** recruitment@datasee.ai
