from fastapi import APIRouter
from src.services.asset_repository_service import AssetRepositoryService
from src.services.fingerprint_compare_service import FingerprintCompareService
from src.services.duplicate_detector_service import DuplicateDetectorService
router=APIRouter(prefix="/assets",tags=["Assets"])
repo=AssetRepositoryService()
duplicate_detector = DuplicateDetectorService()
compare= FingerprintCompareService()

@router.get("/{asset_id}")
def get_asset(asset_id:str):
    return repo.get(asset_id) or {"error":"Not found"}

@router.get("/compare/{source}/{target}")
def compare_fingerprints(source: str, target: str):
    return compare.compare(source, target)    

@router.get("/duplicates/{asset_id}")
def detect_duplicates(asset_id: str):
    return duplicate_detector.detect_duplicates(asset_id)