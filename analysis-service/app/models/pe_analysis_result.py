from dataclasses import dataclass

from app.models.executable import Executable
from app.models.section_data import SectionData



@dataclass
class PEAnalysisResult:

    executable: Executable
    sections: list[SectionData]
    imports: list
    
    