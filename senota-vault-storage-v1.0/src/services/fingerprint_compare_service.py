from src.fingerprint.similarity import Similarity

class FingerprintCompareService:
    def compare(self, source:str, target:str)->dict:
        d=Similarity.distance(source,target)
        return {
            'distance': d,
            'identical': d==0,
            'likely_match': d<=5
        }
