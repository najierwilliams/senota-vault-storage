from fastapi import APIRouter
from src.routes.root_router import router as root_router
from src.routes.upload_router import router as upload_router
from src.routes.asset_router import router as asset_router
from src.routes.asset_lookup_router import router as lookup_router
from src.routes.asset_library_router import router as library_router
from src.routes.info_router import router as info_router
from src.routes.fingerprint_database_router import router as fingerprint_router

router=APIRouter()
router.include_router(root_router)
router.include_router(info_router)
router.include_router(upload_router)
router.include_router(asset_router)
router.include_router(lookup_router)
router.include_router(library_router)
router.include_router(fingerprint_router)
