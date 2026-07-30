from app.analyzers.entropy_analyzer import EntropyAnalyzer




class EntropyService:

    def __init__(self):
        self.analyzer = EntropyAnalyzer()

    def analyze_file(self, data: bytes) -> float:
        return self.analyzer.calculate(data)

    def analyze_sections(self, sections):
        for section in sections:

            section.entropy = (self.analyzer.calculate(section.content))