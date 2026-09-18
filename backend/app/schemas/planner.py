from pydantic import BaseModel, Field


class ResearchSubquestion(BaseModel):
    question: str = Field(min_length=1)
    search_queries: list[str] = Field(min_length=1)
    priority: int = Field(ge=1, le=5)


class ResearchPlan(BaseModel):
    original_question: str = Field(min_length=1)
    subquestions: list[ResearchSubquestion] = Field(min_length=1)