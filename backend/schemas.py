from pydantic import BaseModel

class PatientInput(BaseModel):
    age: int
    gender: int
    family_history: int