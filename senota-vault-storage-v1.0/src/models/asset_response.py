from pydantic import BaseModel

class AssetResponse(BaseModel):
    asset_id:str
    status:str
    message:str
