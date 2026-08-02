from capstone import Cs, CS_ARCH_X86, CS_MODE_64

from app.models.instruction_data import InstructionData



class CapstoneDisassembler:

    def __init__(self):
        self.disassembler = Cs(CS_ARCH_X86, CS_MODE_64)


    def disassemble(self, code: bytes, address: int) -> list[InstructionData]:

        instructions = []

        for instruction in self.disassembler.disasm(code, address):

            instructions.append(
                InstructionData(
                    address=instruction.address,
                    mnemonic=instruction.mnemonic,
                    operands=instruction.op_str
                )
            )

        return instructions