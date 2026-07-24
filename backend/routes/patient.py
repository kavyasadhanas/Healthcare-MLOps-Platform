from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import Patient
from backend.schemas import PatientCreate

router = APIRouter()


@router.post("/patients")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):

    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        family_history=patient.family_history
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient added successfully",
        "patient_id": new_patient.id
    }
@router.get("/patients")
def get_patients(db: Session = Depends(get_db)):

    patients = db.query(Patient).all()

    return patients