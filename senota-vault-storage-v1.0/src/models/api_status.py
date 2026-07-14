from pydantic import BaseModel

class APIStatus(BaseModel):
    status: str
    version: str
    ready: bool
