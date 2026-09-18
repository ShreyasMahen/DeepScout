import httpx

from app.core.config import settings
from app.schemas.source import Source


TAVILY_SEARCH_URL = "https://api.tavily.com/search"


def search_web(
    query: str,
    subquestion: str = "",
    max_results: int = 5,
) -> list[Source]:
    response = httpx.post(
        TAVILY_SEARCH_URL,
        json={
            "api_key": settings.tavily_api_key,
            "query": query,
            "search_depth": "basic",
            "max_results": max_results,
        },
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()
    results = data.get("results", [])

    sources = []

    for result in results:
        source = Source(
            title=result.get("title", ""),
            url=result.get("url", ""),
            snippet=result.get("content", ""),
            provider="tavily",
            search_query=query,
            subquestion=subquestion,
        )
        sources.append(source)

    return sources