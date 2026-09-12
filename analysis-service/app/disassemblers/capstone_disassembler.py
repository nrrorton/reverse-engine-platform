from capstone import (
    Cs, CS_ARCH_X86, CS_MODE_64, CS_GRP_CALL, CS_GRP_JUMP
)
from capstone.x86 import X86_OP_IMM

from app.models.instruction_data import InstructionData, CallType



class CapstoneDisassembler:

    def __init__(self):
        self.disassembler = Cs(CS_ARCH_X86, CS_MODE_64)
        self.disassembler.detail = True


    def disassemble(self, code: bytes, address: int) -> list[InstructionData]:

        instructions = []

        for instruction in self.disassembler.disasm(code, address):

            target = self._get_instruction_target(instruction)
            call_type = self._get_call_type(instruction)

            instructions.append(
                InstructionData(
                    address=instruction.address,
                    mnemonic=instruction.mnemonic,
                    operands=instruction.op_str,
                    size=instruction.size,
                    target=target,
                    call_type=call_type
                )
            )

        return instructions


    def _get_instruction_target(self, instruction) -> int | None:

        if (instruction.group(CS_GRP_CALL) or instruction.group(CS_GRP_JUMP)):

            for operand in instruction.operands:
                if operand.type == X86_OP_IMM:
                    return operand.imm

        return None


    def _get_call_type(self, instruction) -> CallType | None:

        if not instruction.group(CS_GRP_CALL):
            return None

        for operand in instruction.operands:
            if operand.type == X86_OP_IMM:
                return CallType.DIRECT

        return CallType.INDIRECT

