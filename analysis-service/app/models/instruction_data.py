from dataclasses import dataclass



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
    