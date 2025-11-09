# ☀️ Solar Panel Site Analyzer

**Datasee.AI Full-Stack Developer Assessment**

This is a complete full-stack web application built to identify and analyze potential sites for solar panel installations. The entire stack (Vue.js Frontend, FastAPI Backend, and MySQL Database) is fully containerized with Docker, allowing for a one-command setup ``` docker compose up -d``` and deployment.

**Application URL (for local deployment):** [**http://localhost:5173**](http://localhost:5173)

---

##  Core Features

* **Interactive Map:** 50 sample sites are loaded and displayed on an interactive Leaflet.js map, color-coded by their final suitability score.
* **Site Detail Modal:** Clicking any site on the map or table opens a modal with a detailed breakdown of its individual scores (Solar, Area, Grid, etc.) and raw data.
* **Dynamic Weight Analysis:** A set of sliders allows the user to adjust the weights for each of the 5 scoring criteria. Clicking "Re-Analyze" triggers a `POST` request, updates the weights in the database, recalculates all 50 site scores, and refreshes the entire dashboard.
* **Real-time Filtering:** Filter the map and table by `min_score` and `max_score` using range sliders.
* **Analytics Dashboard:** The dashboard includes KPI cards (Total Sites, Avg. Score, Top Score) and a Chart.js bar chart showing the distribution of scores.
* **CSV Export:** A "Export Filtered (CSV)" button triggers a download of the sites currently visible in the table.
* **Fully Containerized:** The entire application (Frontend, Backend, DB) is orchestrated with `docker-compose` for simple, reliable deployment.

---

## 🛠️ Technical Stack

| Category | Technology |
| :--- | :--- |
| **Frontend** | Vue 3 (Composition API), Vue Router, Leaflet.js, Chart.js |
| **Backend** | FastAPI, Python 3.11, SQLAlchemy, Pydantic |
| **Database** | MySQL 8.0 (with Stored Procedures) |
| **Containerization**| Docker & Docker Compose |
| **Web Server** | Nginx (serves the Vue app and proxies the API) |

---

##  Architecture

The application runs as three separate services orchestrated by `docker-compose.yml`:

[Image of a Docker Compose architecture with three services: a Vue frontend in an Nginx container, a FastAPI backend, and a MySQL database, showing network connections]

1.  **`frontend` (Vue.js + Nginx):** A multi-stage `Dockerfile` builds the Vue app into static assets, which are then served by a lightweight Nginx container. The Nginx server also acts as a reverse proxy, forwarding all `/api` requests to the `backend` service, which resolves all CORS issues.
2.  **`backend` (FastAPI):** A Python container running the FastAPI application with Uvicorn. It connects to the `db` service using the internal Docker network name. It exposes port 8000.
3.  **`db` (MySQL):** A standard MySQL 8.0 container. On its first launch, it automatically discovers and runs the SQL scripts located in the `./database` folder. This single step creates the schema, tables, views, and stored procedures, and populates the `sites` table with all 50 sample data points.

---

##  How to Run (Local Setup)

**Prerequisites:**
* [Docker](https://www.docker.com/get-started/) and Docker Compose must be installed and running.
* [Git](https://git-scm.com/) (for cloning).

**1. Clone the Repository**
```bash
git clone https://github.com/vishvesh11/solar-site-data.git
cd solar-analyzer-project
