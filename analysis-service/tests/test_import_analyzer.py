from app.analyzers.import_analyzer import ImportAnalyzer

from app.models.import_data import ImportData, ImportedFunction



def test_known_import_is_enriched():

    imports = [
        ImportData(
            library='KERNEL32.dll',
            functions=[
                ImportedFunction(
                    name='VirtualProtect'
                )
            ]
        )
    ]

    analyzer = ImportAnalyzer()
    result = analyzer.analyze(imports)
    function = result[0].functions[0]

    assert function.category == 'Memory Management'
    assert function.risk == 'Medium'


def test_unknown_import_remains_unknown():

    imports = [
        ImportData(
            library='UNKNOWN.dll',
            functions=[
                ImportedFunction(
                    name='SomethingImMakingUp'
                )
            ]
        )
    ]

    analyzer = ImportAnalyzer()
    result = analyzer.analyze(imports)
    function = result[0].functions[0]

    assert function.category is None
    assert function.description is None
    assert function.risk is None


def test_empty_imports_returns_empty():

    analyzer = ImportAnalyzer()
    result = analyzer.analyze([])

    assert result == []