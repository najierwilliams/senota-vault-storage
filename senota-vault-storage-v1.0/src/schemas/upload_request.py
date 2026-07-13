from pydantic import BaseModel

class UploadRequest(BaseModel):
    customer_id:str
    secure_vault:bool=False
