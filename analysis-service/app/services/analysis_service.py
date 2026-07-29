from fastapi import UploadFile

from app.analyzers.pe_analyzer import PEAnalyzer
from app.analyzers.string_analyzer import StringAnalyzer
from app.analyzers.entropy_analyzer import EntropyAnalyzer

from app.services.file_service import FileService
from app.services.hash_service import HashService

from app.schemas.analysis import AnalysisResponse
from app.schemas.entropy import EntropyResponse, SectionEntropyResponse

from app.mappers.string_mapper import StringMapper
from app.mappers.executable_mapper import ExecutableMapper



class AnalysisService:

    def __init__(self):
        self.file_service = FileService()
        self.hash_service = HashService()

        self.pe_analyzer = PEAnalyzer()
        self.string_analyzer = StringAnalyzer()
        self.entropy_analyzer = EntropyAnalyzer()

        self.string_mapper = StringMapper()
        self.executable_mapper = ExecutableMapper()


    def analyze(self, upload_file: UploadFile):
        with self.file_service.temporary_file(upload_file) as path:

            file_hash = self.hash_service.sha256(path)

            pe_result = self.pe_analyzer.analyze(
                path, upload_file.filename, file_hash
            )

            string_result = self.string_analyzer.analyze(path)

            strings = self.string_mapper.map_strings(string_result.strings)

            with open(path, 'rb') as binary_file:
                data = binary_file.read()
            file_entropy = self.entropy_analyzer.calculate(data)

            section_entropy = []

            for section in pe_result.section_data:
                entropy = self.entropy_analyzer.calculate(section.content)
                section_entropy.append(
                    SectionEntropyResponse(
                        name=section.name, entropy=entropy
                    )
                )

            return AnalysisResponse(
                status='completed',
                executable=self.executable_mapper.map_executable(
                    pe_result.executable
                ),
                sections=pe_result.sections,
                imports=pe_result.imports,
                functions=[],
                strings=strings,
                entropy=EntropyResponse(
                    file_entropy=file_entropy, sections=section_entropy
                )
            )