from app.models.import_data import ImportData

from app.intelligence.import_knowledge import IMPORT_KNOWLEDGE



class ImportAnalyzer:

    def analyze(self, imports: list[ImportData]) -> list[ImportData]:

        for imp in imports:

            for function in imp.functions:

                knowledge = IMPORT_KNOWLEDGE.get(function.name)

                if knowledge:

                    function.category = knowledge['category']
                    function.description = knowledge['description']
                    function.risk = knowledge['risk']

        return imports