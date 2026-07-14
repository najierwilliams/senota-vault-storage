from src.services.asset_service import AssetService

class UploadPipelineService:
    def __init__(self):
        self.assets=AssetService()

    async def process_upload(self,customer_id,upload_file):
        asset=self.assets.create_asset_record(customer_id,upload_file.filename,upload_file.content_type or "application/octet-stream")
        return {"success":True,"asset_id":asset.asset_id,"filename":upload_file.filename,"next_step":"Metadata and fingerprint processing"}
