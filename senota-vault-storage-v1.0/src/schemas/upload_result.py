from pydantic import BaseModel

class UploadResult(BaseModel):
    asset_id:str
    fingerprint:str|None=None
    message:str
