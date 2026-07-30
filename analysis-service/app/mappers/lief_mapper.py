from app.models.import_data import (ImportData, ImportedFunction)



class LIEFMapper:
    
    def map_imports(self, binary):

        imports = []

        for library in binary.imports:
            functions = []

            for entry in library.entries:
                if entry.name:
                    functions.append(ImportedFunction(name=entry.name))
            imports.append(
                ImportData(
                    library=library.name,
                    functions=functions
                )
            )

        return imports
