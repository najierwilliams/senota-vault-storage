"""
SENOTA Vault Storage
Fingerprint Service v1.0

Generates perceptual fingerprints using Pillow + ImageHash.
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from PIL import Image
import imagehash


@dataclass
class FingerprintResult:
    algorithm: str
    fingerprint: str
    generated_at: datetime


class FingerprintService:
    """Generate perceptual image fingerprints."""

    def generate_phash(self, image_path: str) -> FingerprintResult:
        with Image.open(Path(image_path)) as img:
            fp = imagehash.phash(img)

        return FingerprintResult(
            algorithm="phash",
            fingerprint=str(fp),
            generated_at=datetime.utcnow(),
        )

    def generate_all(self, image_path: str) -> dict:
        """Future expansion point for multiple fingerprint algorithms."""
        return {
            "phash": self.generate_phash(image_path)
        }
