from dataclasses import dataclass



@dataclass
class ImportedFunction:

    name: str
    category: str | None = None
    description: str | None = None
    risk: str | None = None



@dataclass
class ImportData:

    library: str
    functions: list[ImportedFunction]