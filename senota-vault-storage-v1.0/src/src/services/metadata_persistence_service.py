class MetadataPersistenceService:
    """Temporary persistence layer until Supabase is connected."""
    def save(self, asset_id:str, metadata:dict):
        return {"asset_id":asset_id,"saved":True,"metadata":metadata}
