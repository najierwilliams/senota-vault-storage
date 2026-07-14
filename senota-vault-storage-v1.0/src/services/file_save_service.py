from pathlib import Path
import shutil

class FileSaveService:
    def __init__(self):
        self.upload_dir=Path("uploads")
        self.upload_dir.mkdir(exist_ok=True)

    def save(self, upload_file):
        destination=self.upload_dir / upload_file.filename
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        return str(destination)
