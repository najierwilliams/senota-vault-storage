from src.db.in_memory_asset_store import STORE

class AssetRepositoryService:

    def save(self, asset):
        STORE.save(asset['asset_id'], asset)
        return asset

    def get(self, asset_id):
        return STORE.get(asset_id)

    def get_all(self):
        return STORE.assets.values()
