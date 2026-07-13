from pydantic import BaseModel

class SecureVaultModel(BaseModel):
    asset_id:str
    encrypted:bool
    key_id:str|None=None
    storage_location:str|None=None
