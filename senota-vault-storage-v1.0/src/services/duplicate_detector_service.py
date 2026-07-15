from src.services.asset_repository_service import AssetRepositoryService
from src.fingerprint.similarity import Similarity


class DuplicateDetectorService:

    def __init__(self):
        self.repo = AssetRepositoryService()

    def detect_duplicates(self, asset_id: str):

        asset = self.repo.get(asset_id)

        if not asset:
            return {
                "success": False,
                "message": "Asset not found"
            }

        if "fingerprints" not in asset:
            return {
                "success": False,
                "message": "Asset has no fingerprints"
            }

        source_hash = asset["fingerprints"]["phash"].fingerprint

        matches = []

        for other in self.repo.get_all():

            if other["asset_id"] == asset_id:
                continue

            if "fingerprints" not in other:
                continue

            target_hash = other["fingerprints"]["phash"].fingerprint

            distance = Similarity.distance(source_hash, target_hash)

            matches.append({
                "asset_id": other["asset_id"],
                "distance": int(distance),
                "identical": bool(distance == 0),
                "likely_match": bool(distance <= 8)
            })

        matches.sort(key=lambda x: x["distance"])

        return {
            "success": True,
            "asset_id": asset_id,
            "duplicates": matches
        }