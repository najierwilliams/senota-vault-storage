class AssetMapper:
    @staticmethod
    def to_dict(asset):
        return asset.__dict__ if hasattr(asset,'__dict__') else dict(asset)
