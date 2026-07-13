import imagehash

class Similarity:
    @staticmethod
    def distance(hash1:str, hash2:str)->int:
        return imagehash.hex_to_hash(hash1)-imagehash.hex_to_hash(hash2)

    @staticmethod
    def identical(hash1:str, hash2:str)->bool:
        return Similarity.distance(hash1,hash2)==0
