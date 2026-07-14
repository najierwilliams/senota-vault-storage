from src.utils.mime_types import ALLOWED_IMAGE_TYPES

class ValidationService:
    def validate(self, content_type:str):
        if content_type not in ALLOWED_IMAGE_TYPES:
            raise ValueError(f"Unsupported content type: {content_type}")
        return True
