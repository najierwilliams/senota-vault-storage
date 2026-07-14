from fastapi import APIRouter
from src.services.database_health_service import DatabaseHealthService

router=APIRouter(prefix="/system",tags=["System"])
svc=DatabaseHealthService()

@router.get("/health")
def health():
    return {"api":"ok","database":svc.check()}
