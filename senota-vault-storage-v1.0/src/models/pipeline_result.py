from pydantic import BaseModel

class PipelineResult(BaseModel):
    success: bool
    file_path: str
    checksum: str
