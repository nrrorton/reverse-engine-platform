from app.schemas.analysis import (
    AnalysisResponse, ExecutableInfo, Section, Import,
    Function, ExtractedString
)


class MockAnalyzer:

    def analyze(self, filename: str) -> AnalysisResponse:

        return AnalysisResponse(
            status='completed',
            executable=ExecutableInfo(
                name=filename,
                architecture='x64',
                entry_point='0x140001000'
            ),
            sections=[
                Section(
                    name='.text',
                    virtual_address='0x1000',
                    raw_offset=1024,
                    size=4096
                ),
                Section(
                    name='.data',
                    virtual_address='0x2000',
                    raw_offset=5120,
                    size=2048
                )
            ],
            imports=[
                Import(
                    library='kernel32.dll',
                    function='CreateFileA'
                ),
                Import(
                    library='kernel32.dll',
                    function='ReadFile'
                )
            ],
            functions=[
                Function(
                    address='0x140001000',
                    size=120,
                    name='main'
                )
            ],
            strings=[
                ExtractedString(
                    address='0x140003000',
                    value='config.ini'
                ),
                ExtractedString(
                    address='0x140003020',
                    value='Hello World'
                )
            ]
        )