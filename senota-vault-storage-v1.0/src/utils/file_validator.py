from pathlib import Path

ALLOWED={".jpg",".jpeg",".png",".webp",".gif"}

class FileValidator:
    @staticmethod
    def validate(filename:str):
        ext=Path(filename).suffix.lower()
        if ext not in ALLOWED:
            raise ValueError(f"Unsupported file type: {ext}")
        return True
