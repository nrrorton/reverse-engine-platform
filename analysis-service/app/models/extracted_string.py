from dataclasses import dataclass



@dataclass(frozen=True)
class ExtractedString:
    '''
    Represents a single printable string discovered in a binary.
    '''

    value: str
    length: int