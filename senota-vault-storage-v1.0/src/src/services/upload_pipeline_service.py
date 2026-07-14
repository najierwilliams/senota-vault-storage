from src.services.asset_service import AssetService
from src.services.processing_pipeline_service import ProcessingPipelineService
from src.services.metadata_persistence_service import MetadataPersistenceService
from src.services.fingerprint_persistence_service import FingerprintPersistenceService

class UploadPipelineService:
    def __init__(self):
        self.assets=AssetService()
        self.pipeline=ProcessingPipelineService()
        self.meta=MetadataPersistenceService()
        self.fp=FingerprintPersistenceService()

    async def process_upload(self,customer_id,upload_file):
        asset=self.assets.create_asset_record(customer_id,upload_file.filename,upload_file.content_type or "application/octet-stream")
        result=self.pipeline.process(upload_file)
        self.meta.save(asset.asset_id,result["metadata"].__dict__)
        self.fp.save(asset.asset_id,result["fingerprints"])
        return {
            "success":True,
            "asset_id":asset.asset_id,
            **result
        }
