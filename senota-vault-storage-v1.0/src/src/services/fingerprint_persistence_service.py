class FingerprintPersistenceService:
    def save(self, asset_id:str, fingerprints:dict):
        return {"asset_id":asset_id,"saved":True,"count":len(fingerprints)}
