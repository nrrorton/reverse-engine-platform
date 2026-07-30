from app.analyzers.entropy_analyzer import EntropyAnalyzer

from app.models.section_data import SectionData



def test_section_contains_entropy():

    section = SectionData(
        name='.text',
        virtual_address='0x1000',
        virtual_size=100,
        raw_offset=512,
        size=100,
        content=b'AAAA'
    )

    analyzer = EntropyAnalyzer()
    section.entropy = analyzer.calculate(section.content)

    assert section.name == '.text'
    assert section.entropy == 0.0


def test_sections_store_individual_entropy_values():

    sections = [
        SectionData(
            name='.text',
            virtual_address='0x1000',
            virtual_size=100,
            raw_offset=512,
            size=100,
            content=b'AAAAAAAAAA'
        ),
        SectionData(
            name='.data',
            virtual_address='0x2000',
            virtual_size=100,
            raw_offset=1024,
            size=100,
            content=bytes(range(100))
        )
    ]

    analyzer = EntropyAnalyzer()

    for section in sections:
        section.entropy = analyzer.calculate(section.content)

    assert sections[0].entropy != sections[1].entropy
    assert sections[0].entropy == 0.0