from app.models.section_data import SectionData

from app.schemas.sections import SectionInfo



class SectionMapper:

    def map_sections(self, sections: list[SectionData]) -> list[SectionInfo]:

        return [
            SectionInfo(
                name=section.name,
                virtual_address=hex(section.virtual_address),
                virtual_size=section.virtual_size,
                raw_offset=section.raw_offset,
                size=section.size,
                entropy=section.entropy
            )
            for section in sections
        ]