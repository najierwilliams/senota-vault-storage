from fastapi import APIRouter, UploadFile

router=APIRouter(prefix="/assets",tags=["Assets"])

@router.post("/upload")
async def upload_asset(file: UploadFile):
    return {"message":"Upload pipeline scaffold","filename":file.filename}
