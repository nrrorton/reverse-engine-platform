from dataclasses import dataclass



@dataclass(frozen=True)
class ExtractedString:
    '''
    Represents a single printable string discovered in a binary.
    '''

    offset: int
    value: str
    length: int
