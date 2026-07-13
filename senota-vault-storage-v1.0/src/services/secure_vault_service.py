from src.security.key_manager import KeyManager
from src.security.vault_policy import VaultPolicy

class SecureVaultService:
    def __init__(self):
        self.keys=KeyManager()

    def prepare(self, secure_vault: bool):
        if not VaultPolicy.archive_enabled(secure_vault):
            return {"enabled":False}
        return {
            "enabled":True,
            "key_id":self.keys.generate_key_id()
        }
