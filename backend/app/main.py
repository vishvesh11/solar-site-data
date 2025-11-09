from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import sites
from .core.config import settings
from .db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Solar Panel Site Analyzer API",
    description="API for the Datasee.AI technical assessment.",
    version="1.0.0"
)

# Cors settings (restricted)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CLIENT_ORIGIN_URL],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# --- Include API Routers ---
app.include_router(sites.router, tags=["Main API"])

@app.get("/", tags=["Root"])
def read_root():
    return {"status": "ok", "message": "WORKING!!"}