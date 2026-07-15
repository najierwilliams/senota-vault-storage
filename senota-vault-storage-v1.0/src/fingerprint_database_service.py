from datetime import datetime
import uuid


class FingerprintDatabaseService:

    def __init__(self):
        self.database = {}

    def add(
        self,
        asset_id,
        customer_id,
        algorithm,
        fingerprint,
    ):

        fingerprint_id = str(uuid.uuid4())

        record = {
            "fingerprint_id": fingerprint_id,
            "asset_id": asset_id,
            "customer_id": customer_id,
            "algorithm": algorithm,
            "fingerprint": fingerprint,
            "created_at": datetime.utcnow().isoformat(),
        }

        self.database[fingerprint_id] = record

        return record

    def get_all(self):
        return list(self.database.values())

    def find_by_asset(self, asset_id):
        return [
            record
            for record in self.database.values()
            if record["asset_id"] == asset_id
        ]

    def find_by_customer(self, customer_id):
        return [
            record
            for record in self.database.values()
            if record["customer_id"] == customer_id
        ]