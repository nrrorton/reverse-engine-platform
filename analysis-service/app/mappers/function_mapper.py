from app.models.function_data import FunctionData

from app.schemas.analysis import Function



class FunctionMapper:

    def map_functions(self, functions: list[FunctionData]) -> list[Function]:

        return [
            Function(
                id=function.id,
                address=hex(function.address),
                size=function.size,
                name=function.name
            )
            for function in functions
        ]