from pydantic import BaseModel
class UploadSummary(BaseModel):
    asset_id:str
    checksum:str
    fingerprint_count:int
    status:str
