from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.soil import router as soil_router

app = FastAPI(title="AI Soil Health Analyzer")

# ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(soil_router)
