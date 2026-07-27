from contextlib import contextmanager
from pathlib import Path
from tempfile import NamedTemporaryFile
from collections.abc import Generator

from fastapi import UploadFile

'''
Create a temporary copy of an uploaded file.
The file is auto removed when the context exits,
even if the analysis raises an exception.
'''

class FileService:

    @contextmanager
    def temporary_file(self, upload_file: UploadFile) -> Generator[Path]:

        suffix = Path(upload_file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            contents = upload_file.file.read()
            temp_file.write(contents)
            temp_path = Path(temp_file.name)

        try:
            yield temp_path
        finally:
            temp_path.unlink(missing_ok=True)