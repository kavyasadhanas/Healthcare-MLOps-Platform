from fastapi import APIRouter
from datetime import datetime
import platform

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "service": "GenomicTwinOps API",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@router.get("/system")
def system_info():
    return {
        "project": "GenomicTwinOps",
        "version": "1.0.0",
        "python": platform.python_version(),
        "operating_system": platform.system(),
        "machine": platform.machine()
    }