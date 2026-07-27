from fastapi import APIRouter, UploadFile, File

from app.services.analysis_service import AnalysisService
from app.schemas.analysis import AnalysisResponse


router = APIRouter()

analysis_service = AnalysisService()


@router.post('/analysis', response_model=AnalysisResponse)
async def analyze_file(file: UploadFile = File(...)):

    return analysis_service.analyze(file)