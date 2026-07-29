from pathlib import Path

from app.models.extracted_string import ExtractedString
from app.models.string_analysis_result import StringAnalysisResult



class StringAnalyzer:
    '''
    Extracts printable ASCII strings from binary files.
    '''

    def __init__(self, minimum_length: int = 4):
        self._minimum_length = minimum_length

    def analyze(self, file_path: Path) -> StringAnalysisResult:
        '''
        Analyze a binary file and returning the extracted strings.
        '''

        current_offset = None
        extracted_strings = []
        current_string = []

        with open(file_path, 'rb') as binary_file:

            offset = 0

            while byte := binary_file.read(1):

                if self._is_printable_ascii(byte):

                    if not current_string:
                        current_offset = offset

                    current_string.append(chr(byte[0]))

                else:
                    self._save_string_if_valid(
                        current_offset=current_offset,
                        current_string=current_string,
                        extracted_strings=extracted_strings
                    )

                    current_offset = None

                offset += 1

        # Here we're handling strings ending at EOF
        self._save_string_if_valid(
            current_offset=current_offset,
            current_string=current_string,
            extracted_strings=extracted_strings
        )

        return StringAnalysisResult(
            strings=extracted_strings,
            minimum_length=self._minimum_length
        )

    def _is_printable_ascii(self, byte: bytes) -> bool:

        value = byte[0]
        return 32 <= value <= 126

    def _save_string_if_valid(
            self,
            current_offset: int | None,
            current_string: list[str],
            extracted_strings: list[ExtractedString]
    ) -> None:

        if len(current_string) >= self._minimum_length:

            value = ''.join(current_string)

            extracted_strings.append(
                ExtractedString(
                    offset=current_offset, 
                    value=value, 
                    length=len(value))
            )

        current_string.clear()
        return None
    