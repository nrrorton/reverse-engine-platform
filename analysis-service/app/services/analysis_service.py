from app.analyzers.mock_analyzer import MockAnalyzer
from app.schemas.analysis import AnalysisResponse


class AnalysisService:

    def __init__(self):
        self.analyzer = MockAnalyzer()

    def analyze(self, filename: str) -> AnalysisResponse:
        return self.analyzer.analyze(filename)