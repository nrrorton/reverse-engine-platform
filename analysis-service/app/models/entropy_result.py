from dataclasses import dataclass



@dataclass(frozen=True)
class SectionEntropy:

    name: str
    entropy: float


@dataclass(frozen=True)
class EntropyResult:

    file_entropy: float
    sections: list[SectionEntropy]