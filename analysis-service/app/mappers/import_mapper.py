from app.models.import_data import ImportData

from app.schemas.imports import (ImportInfo, ImportedFunction)



class ImportMapper:

    def map_imports(self, imports: list[ImportData]) -> list[ImportInfo]:

        mapped_imports = []

        for imp in imports:
            mapped_functions = []

            for function in imp.functions:

                mapped_functions.append(
                    ImportedFunction(
                        name=function.name,
                        category=function.category,
                        description=function.description,
                        risk=function.risk
                ))

            mapped_imports.append(
                ImportInfo(
                    library=imp.library, functions=mapped_functions))

        return mapped_imports

