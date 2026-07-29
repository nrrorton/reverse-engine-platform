from pydantic import BaseModel



class SectionEntropyResponse(BaseModel):

    name: str
    entropy: float


class EntropyResponse(BaseModel):

    file_entropy: float
    sections: list[SectionEntropyResponse]