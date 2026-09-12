from dataclasses import dataclass
from enum import Enum



class CallType(Enum):
    DIRECT = 'direct'
    INDIRECT = 'indirect'



@dataclass
class InstructionData:
    '''
    Represents one disassembled machine insruction.
    '''

    address: int
    mnemonic: str
    operands: str
    size: int
    target: int | None = None
    call_type: CallType | None = None
    