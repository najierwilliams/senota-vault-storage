from fastapi import APIRouter
from src.services.asset_repository_service import AssetRepositoryService

router = APIRouter(tags=["Asset Library"])

repo = AssetRepositoryService()


@router.get("/customers/{customer_id}/assets")
def get_customer_assets(customer_id: str):
    assets = repo.get_all()

    customer_assets = [
        asset
        for asset in assets
        if asset.get("customer_id") == customer_id
    ]

    return {
        "success": True,
        "customer_id": customer_id,
        "total_assets": len(customer_assets),
        "assets": customer_assets,
    }