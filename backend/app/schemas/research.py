from pydantic import BaseModel

from app.schemas.planner import ResearchPlan
from app.schemas.source import Source


class ResearchResponse(BaseModel):
    plan: ResearchPlan
    sources: list[Source]