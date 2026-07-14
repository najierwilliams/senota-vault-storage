from fastapi import APIRouter
from src.core.constants import APP_NAME, API_VERSION

router=APIRouter(prefix="/info",tags=["Info"])

@router.get("")
def info():
    return {"application":APP_NAME,"version":API_VERSION}
