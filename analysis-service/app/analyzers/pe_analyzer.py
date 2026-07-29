from pathlib import Path

import lief

from app.models.executable import Executable
from app.models.pe_analysis_result import PEAnalysisResult
from app.models.section_data import SectionData

from app.mappers.lief_mapper import LIEFMapper



class PEAnalyzer:

    def __init__(self):
        self.mapper = LIEFMapper()


    def analyze(
            self, file_path: Path, original_name: str, file_hash: str
        ) -> PEAnalysisResult:

        binary = lief.PE.parse(str(file_path))

        if binary is None:
            raise ValueError("Failed to parse PE executable.")

        section_data = []

        for section in binary.sections:
            section_data.append(SectionData(
                name=section.name, content=bytes(section.content)
            ))

        executable = Executable(
            name=original_name,
            architecture=str(binary.header.machine),
            entry_point_rva=hex(binary.optional_header.addressof_entrypoint),
            sha256=file_hash
        )

        '''
        for section in binary.sections:
            print('--------------------')
            print(section.name)
            print(type(section.content))
            print(len(section.content))
        
        for imp in binary.imports:
            print(f'Import Type: {type(imp)}')
            print(f'Import Dir: {dir(imp)}')
            break

        first_import = next(iter(binary.imports))
        first_entry = next(iter(first_import.entries))

        print(f'First Entry Type: {type(first_entry)}')
        print(f'First Entry Dir: {dir(first_entry)}')
        '''

        return PEAnalysisResult(
            executable=executable,
            sections=self.mapper.map_sections(binary),
            imports=self.mapper.map_imports(binary),
            section_data=section_data
        )