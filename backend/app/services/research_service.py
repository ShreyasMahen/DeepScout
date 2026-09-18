from app.schemas.research import ResearchResponse
from app.schemas.source import Source
from app.services.planner_service import (
    create_research_plan,
    search_research_plan,
)


def research_question(query: str) -> ResearchResponse:
    plan = create_research_plan(query)
    sources = search_research_plan(plan)

    unique_sources: list[Source] = []
    seen_urls: set[str] = set()

    for source in sources:
        normalized_url = source.url.rstrip("/")

        if normalized_url not in seen_urls:
            seen_urls.add(normalized_url)
            unique_sources.append(source)

    return ResearchResponse(
        plan=plan,
        sources=unique_sources,
    )