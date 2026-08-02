from app.models.function_data import FunctionData

from app.schemas.analysis import Function, Instruction



class FunctionMapper:

    def map_functions(self, functions: list[FunctionData]) -> list[Function]:

        return [
            Function(
                id=function.id,
                address=hex(function.address),
                size=function.size,
                name=function.name,
                instructions=[
                    Instruction(
                        address=hex(instruction.address),
                        mnemonic=instruction.mnemonic,
                        operands=instruction.operands
                    )
                    for instruction in function.instructions
                ]
            )
            for function in functions
        ]