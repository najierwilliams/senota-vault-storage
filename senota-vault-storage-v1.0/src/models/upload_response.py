from pydantic import BaseModel

class UploadResponse(BaseModel):
    success:bool
    asset_id:str
    message:str
