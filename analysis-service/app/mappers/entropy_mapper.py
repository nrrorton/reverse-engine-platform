from app.models.entropy_result import (EntropyResult, SectionEntropy)



class EntropyMapper:

    def map_file_entropy(self, file_entropy: float) -> EntropyResult:

        return EntropyResult(file_entropy=file_entropy, sections=[])