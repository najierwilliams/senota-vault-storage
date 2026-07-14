from fastapi import APIRouter
from src.routes.root_router import router as root_router
from src.routes.asset_router import router as asset_router
from src.routes.asset_lookup_router import router as lookup_router
from src.routes.health_router import router as health_router
from src.routes.system_router import router as system_router

router=APIRouter()
router.include_router(root_router)
router.include_router(asset_router)
router.include_router(lookup_router)
router.include_router(health_router)
router.include_router(system_router)
