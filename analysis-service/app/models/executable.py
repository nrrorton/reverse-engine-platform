from dataclasses import dataclass



@dataclass(frozen=True)
class Executable:
    '''
    Represents basic executable metadata.
    '''

    name: str
    architecture: str
    entry_point_rva: int | None
    sha256: str
    