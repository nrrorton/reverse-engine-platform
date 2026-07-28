from dataclasses import dataclass
from typing import List

from app.models.extracted_string import ExtractedString



@dataclass(frozen=True)
class StringAnalysisResult:
    '''
    Represents the complete results of a string scan.
    '''

    strings: List[ExtractedString]
    minimum_length: int

    @property
    def count(self) -> int:
        return len(self.strings)