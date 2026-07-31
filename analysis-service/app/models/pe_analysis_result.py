from dataclasses import dataclass

from app.models.executable import Executable
from app.models.section_data import SectionData
from app.models.function_data import FunctionData
from app.models.import_data import ImportData



@dataclass(frozen=True)
class PEAnalysisResult:

    executable: Executable
    sections: list[SectionData]
    imports: list[ImportData]
    