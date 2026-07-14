class InMemoryAssetStore:
    def __init__(self):
        self.assets={}
    def save(self, asset_id, record):
        self.assets[asset_id]=record
        return record
    def get(self, asset_id):
        return self.assets.get(asset_id)
STORE=InMemoryAssetStore()
