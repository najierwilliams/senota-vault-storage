from src.providers.storage_provider import StorageProvider

class EncryptedStorageProvider(StorageProvider):
    def save(self,*args,**kwargs):
        raise NotImplementedError("Encrypted storage provider to be implemented.")

    def delete(self,*args,**kwargs):
        raise NotImplementedError
