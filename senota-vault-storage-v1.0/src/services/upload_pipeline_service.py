from src.services.asset_service import AssetService
from src.services.processing_pipeline_service import ProcessingPipelineService

class UploadPipelineService:
    def __init__(self):
        self.assets=AssetService()
        self.pipeline=ProcessingPipelineService()

    async def process_upload(self, customer_id, upload_file):
        asset=self.assets.create_asset_record(customer_id,upload_file.filename,upload_file.content_type or "application/octet-stream")
        result=self.pipeline.process(upload_file)
        return {
            "success":True,
            "asset_id":asset.asset_id,
            "metadata":result.get("metadata"),
            "fingerprints":result.get("fingerprints"),
            "checksum":result.get("checksum")
        }
