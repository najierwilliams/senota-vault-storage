from pydantic import BaseModel
from datetime import datetime

class AssetModel(BaseModel):
    asset_id:str
    customer_id:str
    filename:str
    created_at:datetime
