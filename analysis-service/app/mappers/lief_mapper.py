from app.schemas.sections import SectionInfo
from app.schemas.imports import ImportInfo, ImportedFunction



class LIEFMapper:

    def map_sections(self, binary):

        sections = []

        for section in binary.sections:
            sections.append(
                SectionInfo(
                    name=section.name,
                    virtual_address=hex(section.virtual_address),
                    virtual_size=section.virtual_size,
                    size=section.size
                )
            )

        return sections
    

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
