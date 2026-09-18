from fastapi import APIRouter

from app.schemas.research import ResearchResponse
from app.schemas.scout import ScoutRequest
from app.services.research_service import research_question


router = APIRouter()


@router.post("/research", response_model=ResearchResponse)
def research(request: ScoutRequest) -> ResearchResponse:
    return research_question(request.query)