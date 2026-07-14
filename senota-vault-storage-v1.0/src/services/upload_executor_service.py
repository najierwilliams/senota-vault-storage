from src.services.metadata_service import MetadataService
from src.services.fingerprint_service import FingerprintService
from src.fingerprint.checksum import Checksum

class UploadExecutorService:
    def __init__(self):
        self.metadata=MetadataService(); self.fingerprints=FingerprintService()
    def execute(self,image_path:str):
        return {'metadata':self.metadata.extract(image_path),'fingerprints':self.fingerprints.generate_all(image_path),'checksum':Checksum.sha256(image_path)}
