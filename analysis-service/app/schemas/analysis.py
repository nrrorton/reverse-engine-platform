from pydantic import BaseModel

class ExecutableInfo(BaseModel):

    name: str
    architecture: str
    entry_point: str | None = None


class Section(BaseModel):

    name: str
    virtual_address: str
    raw_offset: int
    size: int


class Import(BaseModel):

    library: str
    function: str


class Function(BaseModel):

    address: str
    size: int
    name: str | None = None


class ExtractedString(BaseModel):

    address: str
    value: str


class AnalysisResponse(BaseModel):

    status: str
    executable: ExecutableInfo
    sections: list[Section]
    imports: list[Import]
    functions: list[Function]
    strings: list[ExtractedString]