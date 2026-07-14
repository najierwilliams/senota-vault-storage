from fastapi import FastAPI
from src.routes.asset_router import router as asset_router
from src.routes.health_router import router as health_router

def register_routes(app:FastAPI):
    app.include_router(asset_router)
    app.include_router(health_router)
