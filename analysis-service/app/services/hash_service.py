import hashlib
from pathlib import Path



class HashService:

    def sha256(self, file_path: Path) -> str:

        sha256 = hashlib.sha256()

        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                sha256.update(chunk)

        return sha256.hexdigest()