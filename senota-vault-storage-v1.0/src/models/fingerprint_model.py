from pydantic import BaseModel
from datetime import datetime

class FingerprintModel(BaseModel):
    asset_id:str
    algorithm:str
    value:str
    created_at:datetime
