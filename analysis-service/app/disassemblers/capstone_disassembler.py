from capstone import (
    Cs, CS_ARCH_X86, CS_MODE_64, CS_GRP_CALL, CS_GRP_JUMP
)
from capstone.x86 import X86_OP_IMM

from app.models.instruction_data import InstructionData



class CapstoneDisassembler:

    def __init__(self):
        self.disassembler = Cs(CS_ARCH_X86, CS_MODE_64)
        self.disassembler.detail = True


    def disassemble(self, code: bytes, address: int) -> list[InstructionData]:

        instructions = []

        for instruction in self.disassembler.disasm(code, address):

            instructions.append(
                InstructionData(
                    address=instruction.address,
                    mnemonic=instruction.mnemonic,
                    operands=instruction.op_str,
                    size=instruction.size,
                    target=self._get_instruction_target(instruction)
                )
            )

        return instructions


    def _get_instruction_target(self, instruction) -> int | None:

        if (instruction.group(CS_GRP_CALL) or instruction.group(CS_GRP_JUMP)):

            for operand in instruction.operands:
                if operand.type == X86_OP_IMM:
                    return operand.imm

        return None

