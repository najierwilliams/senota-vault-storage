from src.services.file_save_service import FileSaveService
from src.services.upload_executor_service import UploadExecutorService

class ProcessingPipelineService:
    def __init__(self):
        self.saver=FileSaveService()
        self.executor=UploadExecutorService()

    def process(self, upload_file):
        path=self.saver.save(upload_file)
        return self.executor.execute(path)
