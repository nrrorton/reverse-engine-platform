from fastapi import UploadFile

from app.analyzers.pe_analyzer import PEAnalyzer
from app.analyzers.string_analyzer import StringAnalyzer
from app.analyzers.import_analyzer import ImportAnalyzer
from app.analyzers.function_analyzer import FunctionAnalyzer

from app.services.entropy_service import EntropyService
from app.services.file_service import FileService
from app.services.hash_service import HashService

from app.schemas.analysis import AnalysisResponse

from app.mappers.string_mapper import StringMapper
from app.mappers.executable_mapper import ExecutableMapper
from app.mappers.section_mapper import SectionMapper
from app.mappers.import_mapper import ImportMapper
from app.mappers.function_mapper import FunctionMapper




class AnalysisService:

    def __init__(self):
        self.file_service = FileService()
        self.hash_service = HashService()
        self.entropy_service = EntropyService()

        self.pe_analyzer = PEAnalyzer()
        self.string_analyzer = StringAnalyzer()
        self.import_analyzer = ImportAnalyzer()
        self.function_analyzer = FunctionAnalyzer()

        self.string_mapper = StringMapper()
        self.executable_mapper = ExecutableMapper()
        self.section_mapper = SectionMapper()
        self.import_mapper = ImportMapper()
        self.function_mapper = FunctionMapper()


    def analyze(self, upload_file: UploadFile):
        with self.file_service.temporary_file(upload_file) as path:

            file_hash = self.hash_service.sha256(path)

            pe_result = self.pe_analyzer.analyze(
                path, upload_file.filename, file_hash
            )

            imports = self.import_analyzer.analyze(pe_result.imports)

            functions = self.function_analyzer.analyze(path, pe_result)

            string_result = self.string_analyzer.analyze(path)

            strings = self.string_mapper.map_strings(string_result.strings)

            self.entropy_service.analyze_sections(pe_result.sections)

            return AnalysisResponse(
                status='completed',
                executable=self.executable_mapper.map_executable(
                    pe_result.executable
                ),
                sections=self.section_mapper.map_sections(
                    pe_result.sections
                ),
                imports=self.import_mapper.map_imports(
                    imports
                ),
                functions=self.function_mapper.map_functions(
                    functions
                ),
                strings=strings,
            )