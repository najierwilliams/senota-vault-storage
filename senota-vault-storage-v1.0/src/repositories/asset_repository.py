class AssetRepository:
    """Persistence abstraction. Database implementation added later."""

    def save(self, asset):
        return asset

    def get(self, asset_id:str):
        raise NotImplementedError
