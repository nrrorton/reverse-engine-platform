from pathlib import Path

from app.models.function_data import FunctionData
from app.models.pe_analysis_result import PEAnalysisResult
from app.models.instruction_data import InstructionData

from app.disassemblers.capstone_disassembler import CapstoneDisassembler




class FunctionAnalyzer:

    TERMINATORS = {'ret', 'jmp'}

    def __init__(self):
        self.disassembler = CapstoneDisassembler()

    def analyze(
            self, file_path: Path, pe_result: PEAnalysisResult
    ) -> list[FunctionData]:

        self.functions = []
        self.visited = set()
        self.next_id = 1

        entry_rva = pe_result.executable.entry_point_rva

        if entry_rva is None:
            return []

        self._discover_function(file_path, pe_result, entry_rva)

        return self.functions
    

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
            self, file_path: Path, offset: int, size: int) -> bytes:

        with open(file_path, 'rb') as binary_file:

            binary_file.seek(offset)

            return binary_file.read(size)


    def _find_entry_function(
            self, file_path: Path, pe_result: PEAnalysisResult
        ) -> FunctionData | None:

        if pe_result.executable.entry_point_rva is None:
            return None

        entry_rva = pe_result.executable.entry_point_rva

        section = self._find_section_for_rva(entry_rva, pe_result.sections)

        if section is None:
            return None

        file_offset = self._rva_to_file_offset(entry_rva, section)

        code_bytes = self._extract_bytes(file_path, file_offset, 500)

        instructions = self.disassembler.disassemble(code_bytes, entry_rva)
        instructions = self._find_function_boundary(instructions)

        function_size = self._calculate_function_size(instructions)

        calls = self._extract_call_targets(instructions)

        return self._build_function(
            entry_rva, function_size, instructions, calls
        )


    def _build_function(
            self, address: int, size: int, instructions, calls) -> FunctionData:

        return FunctionData(
            id=1,
            address=address,
            size=size,
            name='entry',
            instructions=instructions,
            calls=calls
        )


    def _find_function_boundary(
            self, instructions: list[InstructionData]
            ) -> list[InstructionData]:


        function_instructions = []

        for instruction in instructions:
            function_instructions.append(instruction)

            if instruction.mnemonic in self.TERMINATORS:
                break

        return function_instructions


    def _calculate_function_size(
            self, instructions: list[InstructionData]) -> int:


        if not instructions:
            return 0

        first = instructions[0]
        last = instructions[-1]

        return (last.address + last.size - first.address)


    def _extract_call_targets(
            self, instructions: list[InstructionData]) -> list[int]:

        targets = []

        for instruction in instructions:

            if (
                instruction.mnemonic == 'call'
                and instruction.target is not None
            ):
                targets.append(instruction.target)

        return targets


    def _discover_function(
            self, file_path: Path, pe_result: PEAnalysisResult, address: int):

        if address in self.visited:
            return

        self.visited.add(address)

        section = self._find_section_for_rva(address, pe_result.sections)
        if section is None:
            return

        file_offset = self._rva_to_file_offset(address, section)

        code_bytes = self._extract_bytes(file_path, file_offset, 500)

        instructions = self.disassembler.disassemble(code_bytes, address)
        instructions = self._find_function_boundary(instructions)

        calls = self._extract_call_targets(instructions)

        function = FunctionData(
            id=self.next_id,
            address=address,
            size=self._calculate_function_size(instructions),
            name=None,
            instructions=instructions,
            calls=calls
        )

        self.functions.append(function)
        self.next_id += 1

        for target in calls:
            self._discover_function(file_path, pe_result, target)
