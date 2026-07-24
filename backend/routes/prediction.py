from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import Patient
from backend.schemas import PatientInput
from backend.services.predictor import predict
from backend.logger import logger

router = APIRouter(tags=["Prediction"])


# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Predict Disease Risk
@router.post("/predict-risk")
def predict_risk(
    patient: PatientInput,
    db: Session = Depends(get_db)
):

    logger.info("Prediction request received")

    # Call predictor
    result = predict(
        patient.age,
        patient.gender,
        patient.family_history
    )

    risk = result["risk"]
    confidence = result["confidence"]
    model_version = result["model_version"]

    # Save prediction to database
    new_patient = Patient(
        age=patient.age,
        gender=patient.gender,
        family_history=patient.family_history,
        predicted_risk=risk
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    logger.info(
        f"Prediction completed | "
        f"Patient ID={new_patient.id} | "
        f"Risk={risk} | "
        f"Confidence={confidence}% | "
        f"Model Version={model_version}"
    )

    return {
        "patient_id": new_patient.id,
        "age": patient.age,
        "gender": patient.gender,
        "family_history": patient.family_history,
        "predicted_risk": risk,
        "confidence": confidence,
        "model_version": model_version
    }