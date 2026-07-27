from pydantic import BaseModel



class ImportedFunction(BaseModel):

    name: str



class ImportInfo(BaseModel):

    library: str
    functions: list[ImportedFunction]