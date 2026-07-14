class AssetLookupService:
    def get_asset(self, asset_id:str):
        return {"asset_id":asset_id,"status":"pending_database"}
