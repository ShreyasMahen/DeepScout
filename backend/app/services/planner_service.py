from openai import OpenAI

from app.core.config import settings
from app.schemas.planner import ResearchPlan


client = OpenAI(api_key=settings.openai_api_key)


def create_research_plan(query: str) -> ResearchPlan:
    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=f"""
You are the research planner for DeepScout.

Create a research plan for the following question:

{query}

Break the question into several useful research subquestions.
For each subquestion:
- make it specific and researchable
- generate useful search-engine-friendly queries
- assign a priority from 1 to 5, where 5 is most important

Do not answer the original question.
Only create the research plan.
""",
        text_format=ResearchPlan,
    )

    return response.output_parsed