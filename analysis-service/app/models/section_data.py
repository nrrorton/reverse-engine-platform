from dataclasses import dataclass



@dataclass
class SectionData:

    name: str
    virtual_address: str
    virtual_size: int
    raw_offset: int
    size: int
    content: bytes

    entropy: float | None = None
    