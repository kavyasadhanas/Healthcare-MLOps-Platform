from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import Patient

router = APIRouter(tags=["History"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()

    return patients