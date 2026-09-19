from pydantic import BaseModel



class Finding(BaseModel):

    title: str
    observation: str
    interpretation: str
    evidence: list[str]
    confidence: str



class AIAnalysis(BaseModel):
    summary: str
    findings: list[Finding]