from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name="SENOTA Vault Storage"
    max_upload_size=50*1024*1024
    secure_vault_default=False

settings=Settings()
