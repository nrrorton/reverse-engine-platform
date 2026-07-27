from pathlib import Path

import lief

from app.schemas.analysis import (AnalysisResponse, ExecutableInfo)
from app.mappers.lief_mapper import LIEFMapper



class PEAnalyzer:

    def __init__(self):
        self.mapper = LIEFMapper()


    def analyze(
            self, file_path: Path, original_name: str, file_hash: str
        ) -> AnalysisResponse:

        binary = lief.PE.parse(str(file_path))

        if binary is None:
            raise ValueError("Failed to parse PE executable.")

        executable = ExecutableInfo(
            name=original_name,
            architecture=str(binary.header.machine),
            entry_point_rva=hex(binary.optional_header.addressof_entrypoint),
            sha256=file_hash
        )
        '''
        for section in binary.sections:
            print(f'Section Type:  {type(section)}')
            print(f'Section Dir: {dir(section)}')
            break

        for imp in binary.imports:
            print(f'Import Type: {type(imp)}')
            print(f'Import Dir: {dir(imp)}')
            break

        first_import = next(iter(binary.imports))
        first_entry = next(iter(first_import.entries))

        print(f'First Entry Type: {type(first_entry)}')
        print(f'First Entry Dir: {dir(first_entry)}')
        '''

        return AnalysisResponse(
            status='completed',
            executable=executable,
            sections=self.mapper.map_sections(binary),
            imports=self.mapper.map_imports(binary),
            functions=[],
            strings=[]
        )