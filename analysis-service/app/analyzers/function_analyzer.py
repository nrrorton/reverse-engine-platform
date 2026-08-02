from pathlib import Path

from app.models.function_data import FunctionData
from app.models.pe_analysis_result import PEAnalysisResult

from app.disassemblers.capstone_disassembler import CapstoneDisassembler



class FunctionAnalyzer:

    def __init__(self):
        self.disassembler = CapstoneDisassembler()

    def analyze(
            self, file_path: Path, pe_result: PEAnalysisResult
    ) -> list[FunctionData]:

        if pe_result.executable.entry_point_rva is None:
            return []

        entry_rva = pe_result.executable.entry_point_rva

        section = self._find_section_for_rva(entry_rva, pe_result.sections)
        if section is None:
            return []

        file_offset = self._rva_to_file_offset(entry_rva, section)

        code_bytes = self._extract_bytes(file_path, file_offset)

        instructions = self.disassembler.disassemble(
            code_bytes, entry_rva)

        print(f'Disassembled {len(instructions)} instructions')
        for instruction in instructions:
            print(hex(instruction.address), instruction.mnemonic, instruction.operands)

        entry_function = FunctionData(
            id=1, 
            address=entry_rva,
            size=None,
            name='entry',
            instructions=instructions
        )

        return [entry_function]


    def _find_section_for_rva(self, rva: int, sections):

        for section in sections:

            section_start = section.virtual_address
            section_end = (section.virtual_address + section.virtual_size)

            if section_start <= rva < section_end:
                return section

        return None


    def _rva_to_file_offset(self, rva: int, section) -> int:

        offset_into_section = (rva - section.virtual_address)

        return (section.raw_offset + offset_into_section)


    def _extract_bytes(
            self, file_path: Path, offset: int, size: int=100) -> bytes:

        with open(file_path, 'rb') as binary_file:

            binary_file.seek(offset)

            return binary_file.read(size)