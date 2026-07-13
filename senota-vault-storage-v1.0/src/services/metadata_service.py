"""
SENOTA Vault Storage
Metadata Service v1.0

Responsible for extracting and normalizing metadata from uploaded assets.
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from PIL import Image


@dataclass
class ImageMetadata:
    filename: str
    extension: str
    width: int
    height: int
    color_mode: str
    file_size: int
    extracted_at: datetime


class MetadataService:
    """Extract metadata from uploaded images."""

    def extract(self, image_path: str) -> ImageMetadata:
        path = Path(image_path)

        with Image.open(path) as img:
            return ImageMetadata(
                filename=path.name,
                extension=path.suffix.lower(),
                width=img.width,
                height=img.height,
                color_mode=img.mode,
                file_size=path.stat().st_size,
                extracted_at=datetime.utcnow(),
            )
