from dataclasses import dataclass



@dataclass(frozen=True)
class SectionData:

    name: str
    content: bytes
    