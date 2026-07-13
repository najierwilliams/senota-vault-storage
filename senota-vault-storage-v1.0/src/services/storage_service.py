"""
SENOTA Vault Storage
Storage Service v1.0

Abstraction layer for asset storage.
Future providers:
- Local
- Cloud object storage
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class StorageResult:
    success: bool
    location: str


class StorageService:
    def __init__(self, base_directory: str = "storage"):
        self.base_directory = Path(base_directory)
        self.base_directory.mkdir(parents=True, exist_ok=True)

    def save(self, asset_id: str, data: bytes) -> StorageResult:
        destination = self.base_directory / f"{asset_id}.bin"
        destination.write_bytes(data)
        return StorageResult(True, str(destination))

    def delete(self, location: str) -> bool:
        path = Path(location)
        if path.exists():
            path.unlink()
            return True
        return False
