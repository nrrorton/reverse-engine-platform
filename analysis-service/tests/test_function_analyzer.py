from pathlib import Path

from app.analyzers.function_analyzer import FunctionAnalyzer
from app.models.executable import Executable
from app.models.pe_analysis_result import PEAnalysisResult
from app.models.section_data import SectionData



def test_discovers_called_function_and_relationship(tmp_path):

    code = bytes.fromhex(
        'e805000000'        # call 0x100a
        'c3'                # ret
        '90'                # padding
        '90'
        '90'
        '90'
        '90'                # 0x100a: nop
        'c3'                # 0x100b: ret
    )

    file_path = tmp_path / 'test.bin'
    file_path.write_bytes(code)

    executable = Executable(
        name='test.bin',
        architecture='x86-64',
        entry_point_rva=0x1000,
        sha256='test'
    )

    section = SectionData(
        name='.text',
        virtual_address=0x1000,
        virtual_size=len(code),
        raw_offset=0,
        size=len(code),
        content=code
    )

    pe_result = PEAnalysisResult(
        executable=executable,
        sections=[section],
        imports=[]
    )

    analyzer = FunctionAnalyzer()
    functions = analyzer.analyze(file_path, pe_result)

    assert len(functions) == 2

    assert functions[0].address == 0x1000
    assert functions[0].calls == [0x100a]
    assert functions[0].called_function_ids == [2]

    assert functions[1].address == 0x100a
    assert functions[1].calls == []
    assert functions[1].called_function_ids == []



def test_indirect_call_is_not_recursively_discovered(tmp_path):

    code = bytes.fromhex(
        'ff158a000000'          # call qword ptr [rip + 0x8a]
        'c3'                    # ret
    )

    file_path = tmp_path / 'test.bin'
    file_path.write_bytes(code)

    executable = Executable(
        name='test.bin',
        architecture='x86-64',
        entry_point_rva=0x1000,
        sha256='test'
    )

    section = SectionData(
        name='.text',
        virtual_address=0x1000,
        virtual_size=len(code),
        raw_offset=0,
        size=len(code),
        content=code
    )

    pe_result = PEAnalysisResult(
        executable=executable,
        sections=[section],
        imports=[]
    )

    analyzer = FunctionAnalyzer()
    functions = analyzer.analyze(file_path, pe_result)

    assert len(functions) == 1
    assert functions[0].address == 0x1000
    assert functions[0].calls == []
    assert functions[0].called_function_ids == []

    assert functions[0].instructions[0].call_type.value == 'indirect'
    assert functions[0].instructions[0].target is None



def test_no_entry_point_returns_empty_list(tmp_path):

    file_path = tmp_path / 'test.bin'
    file_path.write_bytes(b'')

    executable = Executable(
        name='test.bin',
        architecture='x86-64',
        entry_point_rva=None,
        sha256='test'
    )

    pe_result = PEAnalysisResult(
        executable=executable,
        sections=[],
        imports=[]
    )

    analyzer = FunctionAnalyzer()
    functions = analyzer.analyze(file_path, pe_result)

    assert functions == []



def test_unmapped_entry_point_returns_no_functions(tmp_path):
    code = bytes.fromhex('90c3')

    file_path = tmp_path / 'test.bin'
    file_path.write_bytes(code)

    executable = Executable(
        name='test.bin',
        architecture='x86-64',
        entry_point_rva=0x5000,
        sha256='test'
    )

    section = SectionData(
        name='.text',
        virtual_address=0x1000,
        virtual_size=len(code),
        raw_offset=0,
        size=len(code),
        content=code
    )

    pe_result = PEAnalysisResult(
        executable=executable,
        sections=[section],
        imports=[]
    )

    analyzer = FunctionAnalyzer()
    functions = analyzer.analyze(file_path, pe_result)

    assert functions == []