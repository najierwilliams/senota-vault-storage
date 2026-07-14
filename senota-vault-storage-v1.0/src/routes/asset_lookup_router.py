from fastapi import APIRouter
from src.services.asset_repository_service import AssetRepositoryService
router=APIRouter(prefix="/assets",tags=["Assets"])
repo=AssetRepositoryService()
@router.get("/{asset_id}")
def get_asset(asset_id:str):
    return repo.get(asset_id) or {"error":"Not found"}
