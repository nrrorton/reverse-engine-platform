from dataclasses import dataclass

from app.models.executable import Executable
from app.models.section_data import SectionData



@dataclass(frozen=True)
class PEAnalysisResult:

    executable: Executable
    sections: list
    imports: list
    section_data: list[SectionData]
    