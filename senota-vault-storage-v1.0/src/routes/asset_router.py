from fastapi import APIRouter, UploadFile, File
from src.services.upload_pipeline_service import UploadPipelineService

router=APIRouter(prefix="/assets",tags=["Assets"])
pipeline=UploadPipelineService()

@router.post("/upload")
async def upload(customer_id:str,file:UploadFile=File(...)):
    return await pipeline.process_upload(customer_id,file)
