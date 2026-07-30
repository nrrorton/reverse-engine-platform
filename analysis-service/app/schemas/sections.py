from pydantic import BaseModel



class SectionInfo(BaseModel):

    name: str
    virtual_address: str
    virtual_size: int
    raw_offset: int
    size: int
    entropy: float | None = None
    