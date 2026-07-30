from app.schemas.imports import ImportInfo, ImportedFunction



class LIEFMapper:
    
    def map_imports(self, binary):

        imports = []

        for library in binary.imports:
            functions = []

            for entry in library.entries:
                if entry.name:
                    functions.append(ImportedFunction(name=entry.name))
            imports.append(
                ImportInfo(
                    library=library.name,
                    functions=functions
                )
            )

        return imports
