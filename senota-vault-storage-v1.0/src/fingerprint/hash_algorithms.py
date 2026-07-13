from PIL import Image
import imagehash

class HashAlgorithms:
    @staticmethod
    def generate_all(image_path:str)->dict:
        with Image.open(image_path) as img:
            return {
                'phash': str(imagehash.phash(img)),
                'dhash': str(imagehash.dhash(img)),
                'ahash': str(imagehash.average_hash(img)),
                'whash': str(imagehash.whash(img)),
            }
