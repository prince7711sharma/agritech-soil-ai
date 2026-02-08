from fastapi import APIRouter
from app.schemas.soil_schema import SoilInput
from app.models.soil_ml import classify_soil_fertility
from app.utils.rules import nutrient_status
from app.services.soil_report import build_soil_report
from app.services.llm_service import explain_soil_report

router = APIRouter()

@router.post("/analyze-soil")
def analyze_soil(data: SoilInput):
    fertility = classify_soil_fertility(
        data.nitrogen, data.phosphorus, data.potassium, data.ph
    )

    nutrients = nutrient_status(
        data.nitrogen, data.phosphorus, data.potassium, data.ph
    )

    report = build_soil_report(data, fertility, nutrients)

    return report


@router.post("/explain-soil")
def explain_soil(data: SoilInput):
    fertility = classify_soil_fertility(
        data.nitrogen, data.phosphorus, data.potassium, data.ph
    )

    nutrients = nutrient_status(
        data.nitrogen, data.phosphorus, data.potassium, data.ph
    )

    report = build_soil_report(data, fertility, nutrients)

    explanation = explain_soil_report(report)

    return {
        "soil_report": report,
        "ai_explanation": explanation
    }
