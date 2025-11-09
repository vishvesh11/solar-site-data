
# Full Stack Developer - Technical Assessment Exercise
## Datasee.AI

---

## Assessment Overview

**Type:** Take-home assignment  
**Focus:** Spatial Analysis Web Application

---

## Project Brief: Solar Panel Site Analyzer

Build a web application that helps identify and analyze potential sites for solar panel installations using spatial data analysis. This project simulates a real-world scenario similar to Datasee.AI's work in renewable energy asset management.

---

## Technical Requirements

### Frontend (Angular/Vue3)
- Interactive map interface to display locations
- Dashboard showing analysis results
- Responsive design (mobile and desktop)
- Data visualization charts/graphs
- Form for inputting analysis parameters

### Backend (Django REST Framework/FastAPI)
- RESTful API endpoints for spatial analysis
- Data processing and calculations
- Database operations (MySQL)
- Input validation and error handling

### Spatial Analysis Features
1. **Site Scoring System**: Calculate suitability scores based on:
   - Average solar irradiance (sunshine hours)
   - Available land area
   - Distance from power grid
   - Terrain slope/elevation
   - Proximity to existing infrastructure

2. **Interactive Map**: 
   - Display potential sites as markers/polygons
   - Color-coded based on suitability score
   - Click on sites to view detailed analysis
   - Filter sites by score threshold

3. **Analytics Dashboard**:
   - Top 10 recommended sites
   - Statistical summary (average scores, distributions)
   - Comparison charts
   - Export results as CSV/JSON

---

## Functional Requirements

### Must Have (Core Features)
1. Upload/load provided spatial dataset
2. Display all sites on an interactive map
3. Calculate suitability score for each site
4. Filter and sort sites by various criteria
5. Show detailed information for individual sites
6. Responsive UI that works on desktop and mobile

### Nice to Have (Bonus Features)
1. Draw custom areas on the map for analysis
2. Real-time score recalculation with adjustable weights
3. Comparative analysis between multiple sites
4. Data caching for performance optimization
5. Docker containerization
6. Unit tests for critical functions
7. CI/CD pipeline configuration

---

## Technical Stack (As per JD)

- **Frontend**: Angular or Vue3, HTML5, CSS3, JavaScript
- **Backend**: Django REST Framework or FastAPI, Python
- **Database**: MySQL
- **Map Library**: Leaflet.js or Mapbox GL JS (recommended)
- **Version Control**: Git
- **Optional**: Docker, AWS deployment

---

## Deliverables

1. **Source Code**
   - Well-structured, commented code
   - Git repository with meaningful commit history
   - Separate frontend and backend folders

2. **Documentation**
   - README.md with setup instructions
   - API documentation (endpoints, request/response formats)
   - Architecture diagram or explanation
   - Known limitations and future improvements

3. **Database**
   - SQL schema/migration files
   - Sample data loading script

4. **Deployment (Optional)**
   - Dockerfiles for frontend and backend
   - docker-compose.yml for local development
   - Deployment instructions

---

## Evaluation Criteria

### Code Quality (30%)
- Clean, readable, and maintainable code
- Proper code organization and project structure
- Adherence to best practices and design patterns
- Meaningful variable/function names
- Appropriate comments and documentation

### Functionality (30%)
- All core features implemented and working
- Accurate spatial calculations
- Proper error handling
- Input validation
- User-friendly interface

### Technical Implementation (25%)
- Efficient API design
- Database schema design
- Performance optimization
- Security considerations (SQL injection, XSS prevention)
- Responsive design implementation

### Problem-Solving & Innovation (15%)
- Approach to spatial analysis algorithms
- Creative solutions to challenges
- Bonus features implementation
- Code reusability

---

## Spatial Analysis Formula

Calculate the suitability score (0-100) using weighted average:

```
Suitability Score = (
    solar_irradiance_score * 0.35 +
    area_score * 0.25 +
    grid_distance_score * 0.20 +
    slope_score * 0.15 +
    infrastructure_score * 0.05
)
```

**Individual Score Calculations:**

1. **Solar Irradiance Score** (0-100):
   - 100: >= 5.5 kWh/m²/day
   - Proportional scaling down to 0 for < 3.0 kWh/m²/day

2. **Area Score** (0-100):
   - 100: >= 50,000 m²
   - Proportional scaling down to 0 for < 5,000 m²

3. **Grid Distance Score** (0-100):
   - 100: <= 1 km
   - 0: >= 20 km
   - Linear inverse relationship

4. **Slope Score** (0-100):
   - 100: 0-5 degrees
   - 50: 5-15 degrees
   - 0: > 20 degrees

5. **Infrastructure Score** (0-100):
   - Based on proximity to roads/utilities
   - 100: <= 0.5 km
   - 0: >= 5 km

---

## API Endpoint Specifications

### Required Endpoints

1. **GET /api/sites**
   - Returns all sites with basic information
   - Query parameters: `min_score`, `max_score`, `limit`, `offset`

2. **GET /api/sites/{id}**
   - Returns detailed information for a specific site
   - Includes full analysis breakdown

3. **POST /api/analyze**
   - Triggers recalculation with custom weights
   - Request body: `{ "weights": { "solar": 0.4, "area": 0.3, ... } }`

4. **GET /api/statistics**
   - Returns summary statistics across all sites
   - Average scores, distributions, etc.

5. **GET /api/export**
   - Exports filtered results as CSV or JSON
   - Query parameters: `format`, `min_score`

---

## Setup Instructions for Candidates

1. Clone the provided data repository
2. Set up MySQL database
3. Create virtual environment and install dependencies
4. Run database migrations
5. Load sample data using provided script
6. Start backend server
7. Install frontend dependencies
8. Start frontend development server
9. Access application at http://localhost:4200 (or configured port)

---

## Submission Guidelines

1. **Code Repository**
   - Push code to GitHub/GitLab (public or provide access)
   - Include all necessary files (except credentials)
   - Provide repository link

2. **Documentation**
   - Comprehensive README with setup instructions
   - API documentation
   - Any assumptions or design decisions made

3. **Demo (Optional)**
   - Screen recording or live demo link
   - Walkthrough of key features

4. **Submission Timeline**
   - Complete within 48 hours of receiving assignment
   - Email submission link to recruitment team

---

## Support During Assessment

- Candidates may use online resources, documentation, and AI assistants
- Questions about requirements can be sent via email (response within 4 hours)
- Focus is on problem-solving approach, not memorization

---

## Post-Submission Interview

Selected candidates will be invited for a technical discussion covering:
- Architecture and design decisions
- Challenges faced and solutions implemented
- Code walkthrough
- Potential improvements and scaling considerations
- How the solution could integrate with Datasee.AI's platform

---

## Notes

- This assessment is designed to be completed in 2 days but candidates can demonstrate bonus features if they complete core requirements early
- Code quality and problem-solving approach are valued over feature completeness
- Real-world applicability to Datasee.AI's domain (renewable energy asset management) is a plus
- Partial submissions with good documentation are acceptable if time constraints are an issue

---

**Good luck! We're excited to see your solution.**

For questions, contact: recruitment@datasee.ai
