from pathlib import Path

UPLOAD_DIRECTORY=Path("uploads")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

MAX_UPLOAD_SIZE=50*1024*1024
