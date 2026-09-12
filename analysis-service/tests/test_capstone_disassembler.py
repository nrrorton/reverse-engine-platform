from app.disassemblers.capstone_disassembler import CapstoneDisassembler
from app.models.instruction_data import CallType



def test_disassembles_single_instruction():

    disassembler = CapstoneDisassembler()

    code = bytes.fromhex('90')

    instructions = disassembler.disassemble(code, 0x1000)

    assert len(instructions) == 1
    assert instructions[0].address == 0x1000
    assert instructions[0].mnemonic == 'nop'


def test_direct_call_has_target():

    disassembler = CapstoneDisassembler()

    code = bytes.fromhex('e8fb000000')

    instructions = disassembler.disassemble(code, 0x1000)

    assert len(instructions) == 1
    assert instructions[0].mnemonic == 'call'
    assert instructions[0].target == 0x1100
    assert instructions[0].call_type == CallType.DIRECT


def test_indirect_call_has_no_target():

    disassembler = CapstoneDisassembler()

    code = bytes.fromhex('ff158a000000')

    instructions = disassembler.disassemble(code, 0x1000)

    assert len(instructions) == 1
    assert instructions[0].mnemonic == 'call'
    assert instructions[0].target is None
    assert instructions[0].call_type == CallType.INDIRECT