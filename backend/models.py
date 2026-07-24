from sqlalchemy import Column, Integer, String
from backend.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    age = Column(Integer)
    gender = Column(Integer)
    family_history = Column(Integer)

    predicted_risk = Column(Integer)