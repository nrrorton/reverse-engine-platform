from dataclasses import dataclass, field

from app.models.instruction_data import InstructionData



@dataclass
class FunctionData:
    '''
    Represents a discovered function within an executable.
    '''

    id: int
    address: int
    size: int | None
    name: str | None

    instructions: list[InstructionData] = field(default_factory=list)
    calls: list[int] = field(default_factory=list)