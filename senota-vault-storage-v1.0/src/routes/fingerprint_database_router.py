from fastapi import APIRouter
from src.fingerprint_database_service import FingerprintDatabaseService

router = APIRouter(tags=["Fingerprint Database"])

db = FingerprintDatabaseService()


@router.get("/fingerprints")
def get_all_fingerprints():
    return {
        "success": True,
        "total": len(db.get_all()),
        "fingerprints": db.get_all()
    }


@router.get("/fingerprints/customer/{customer_id}")
def get_customer_fingerprints(customer_id: str):
    fingerprints = db.find_by_customer(customer_id)

    return {
        "success": True,
        "customer_id": customer_id,
        "total": len(fingerprints),
        "fingerprints": fingerprints
    }


@router.get("/fingerprints/asset/{asset_id}")
def get_asset_fingerprints(asset_id: str):
    fingerprints = db.find_by_asset(asset_id)

    return {
        "success": True,
        "asset_id": asset_id,
        "total": len(fingerprints),
        "fingerprints": fingerprints
    }