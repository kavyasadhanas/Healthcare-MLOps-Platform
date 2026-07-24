from fastapi import APIRouter
from backend.services.model_metadata import MODEL_METADATA

router = APIRouter(tags=["Models"])


@router.get("/models")
def get_models():
    return MODEL_METADATA