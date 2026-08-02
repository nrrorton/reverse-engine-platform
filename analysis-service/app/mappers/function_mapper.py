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
                calls=[hex(call) for call in function.calls],
                instructions=[
                    Instruction(
                        address=hex(instruction.address),
                        mnemonic=instruction.mnemonic,
                        operands=instruction.operands,
                        size=instruction.size,
                        target=(
                            hex(instruction.target)
                            if instruction.target is not None
                            else None
                        )
                    )
                    for instruction in function.instructions
                ]
            )
            for function in functions
        ]