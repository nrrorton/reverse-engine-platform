from app.models.extracted_string import ExtractedString as DomainString
from app.schemas.analysis import ExtractedString as StringSchema



class StringMapper:

    def map_strings(self, strings: list[DomainString]) -> list[StringSchema]:

        return [
            StringSchema(
                value=item.value, length=item.length)
                for item in strings]