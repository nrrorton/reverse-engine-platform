from pydantic import BaseModel

from app.schemas.sections import SectionInfo
from app.schemas.imports import ImportInfo




class ExecutableInfo(BaseModel):

    name: str
    architecture: str
    entry_point_rva: str | None = None
    sha256: str


class Section(BaseModel):

    name: str
    virtual_address: int
    raw_offset: int
    size: int


class Import(BaseModel):

    library: str
    function: str


class Function(BaseModel):

    id: int
    address: str
    size: int | None = None
    name: str | None = None


class ExtractedString(BaseModel):

    offset: int
    value: str
    length: int


class AnalysisResponse(BaseModel):

    status: str
    executable: ExecutableInfo
    sections: list[SectionInfo]
    imports: list[ImportInfo]
    functions: list[Function]
    strings: list[ExtractedString]
