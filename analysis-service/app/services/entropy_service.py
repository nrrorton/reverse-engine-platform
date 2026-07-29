from app.analyzers.entropy_analyzer import EntropyAnalyzer

from app.models.entropy_result import (EntropyResult, SectionEntropy)



class EntropyService:

    def __init__(self):
        self.analyzer = EntropyAnalyzer()

    def analyze_file(self, data: bytes) -> float:
        return self.analyzer.calculate(data)

    def analyze_sections(self, sections) -> list[SectionEntropy]:
        results = []

        for section in sections:
            entropy = self.analyzer.calculate(bytes(section.content))

            results.append(SectionEntropy(name=section.name, entropy=entropy))

        return results