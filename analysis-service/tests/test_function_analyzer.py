from app.disassemblers.capstone_disassembler import CapstoneDisassembler



def test_disassembles_single_instruction():

    disassembler = CapstoneDisassembler()

    code = bytes.fromhex('90')

    instructions = disassembler.disassemble(code, 0x1000)

    assert len(instructions) == 1
    assert instructions[0].address == 0x1000
    assert instructions[0].mnemonic == 'nop'