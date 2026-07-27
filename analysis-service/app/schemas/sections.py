from pydantic import BaseModel



class SectionInfo(BaseModel):

    name: str
    virtual_address: str
    virtual_size: int
    size: int
    