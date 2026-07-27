from app.analyzers.pe_analyzer import PEAnalyzer
from app.services.file_service import FileService
from app.services.hash_service import HashService

from fastapi import UploadFile


class AnalysisService:

    def __init__(self):
        self.file_service = FileService()
        self.analyzer = PEAnalyzer()
        self.hash_service = HashService()

    def analyze(self, upload_file: UploadFile):
        with self.file_service.temporary_file(upload_file) as path:
            file_hash = self.hash_service.sha256(path)

            return self.analyzer.analyze(path, upload_file.filename, file_hash)