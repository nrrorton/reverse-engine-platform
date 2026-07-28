from dataclasses import dataclass

from app.models.executable import Executable



@dataclass(frozen=True)
class PEAnalysisResult:

    executable: Executable
    sections: list
    imports: list
    