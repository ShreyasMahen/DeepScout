from fastapi import APIRouter

from app.schemas.scout import ScoutRequest
from app.schemas.planner import ResearchPlan
from app.services.planner_service import create_research_plan


router = APIRouter()


@router.post("/plan", response_model=ResearchPlan)
def plan_research(request: ScoutRequest) -> ResearchPlan:
    return create_research_plan(request.query)