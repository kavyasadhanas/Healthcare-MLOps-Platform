from fastapi import FastAPI

from backend.database import Base, engine

from backend.routes.health import router as health_router
from backend.routes.prediction import router as prediction_router
from backend.routes.history import router as history_router
from backend.routes.model import router as model_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI app
app = FastAPI(
    title="GenomicTwinOps API",
    description="Self-Healing MLOps Platform for Genomic Risk Prediction",
    version="1.0.0"
)


# Home Route
@app.get("/")
def home():
    return {
        "project": "GenomicTwinOps",
        "status": "Running",
        "version": "1.0.0"
    }


# Health APIs
app.include_router(
    health_router,
    prefix="/api/v1"
)


# Prediction APIs
app.include_router(
    prediction_router,
    prefix="/api/v1"
)


# History APIs
app.include_router(
    history_router,
    prefix="/api/v1"
)


# Model Information APIs
app.include_router(
    model_router,
    prefix="/api/v1"
)