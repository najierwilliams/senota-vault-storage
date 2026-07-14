from src.services.asset_service import AssetService
from src.services.processing_pipeline_service import ProcessingPipelineService
from src.services.asset_repository_service import AssetRepositoryService

class UploadPipelineService:
    def __init__(self):
        self.assets=AssetService()
        self.pipeline=ProcessingPipelineService()
        self.repo=AssetRepositoryService()

    async def process_upload(self, customer_id, upload_file):
        asset=self.assets.create_asset_record(customer_id, upload_file.filename, upload_file.content_type or "application/octet-stream")
        result=self.pipeline.process(upload_file)
        response={
            "asset_id":asset.asset_id,
            "customer_id":asset.customer_id,
            "filename":asset.filename,
            "checksum":result["checksum"],
            "metadata":result["metadata"].__dict__,
            "fingerprints":result["fingerprints"],
            "success":True
        }
        self.repo.save(response)
        return response
