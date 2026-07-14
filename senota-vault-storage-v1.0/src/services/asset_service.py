from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class AssetRecord:
    asset_id:str
    customer_id:str
    filename:str
    content_type:str
    created_at:datetime

class AssetService:
    def create_asset_record(self, customer_id:str, filename:str, content_type:str)->AssetRecord:
        return AssetRecord(
            asset_id=str(uuid.uuid4()),
            customer_id=customer_id,
            filename=filename,
            content_type=content_type,
            created_at=datetime.utcnow()
        )
