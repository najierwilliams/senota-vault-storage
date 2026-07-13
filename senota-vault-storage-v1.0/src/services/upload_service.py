from src.services.asset_service import AssetService
from src.services.metadata_service import MetadataService
from src.services.fingerprint_service import FingerprintService

class UploadService:
    def __init__(self):
        self.assets=AssetService()
        self.metadata=MetadataService()
        self.fingerprints=FingerprintService()

    def prepare(self, customer_id:str, image_path:str):
        asset=self.assets.create_asset_record(customer_id,image_path,"image")
        meta=self.metadata.extract(image_path)
        fp=self.fingerprints.generate_all(image_path)
        return {"asset":asset,"metadata":meta,"fingerprints":fp}
