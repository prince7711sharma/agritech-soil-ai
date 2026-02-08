from fastapi import FastAPI
from app.api.soil import router as soil_router

app = FastAPI(title="AI Soil Health Analyzer")

app.include_router(soil_router)
