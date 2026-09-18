from fastapi import APIRouter, Query

from app.schemas.source import Source
from app.services.search_service import search_web


router = APIRouter()


@router.get("/search", response_model=list[Source])
def search(
    query: str = Query(min_length=1),
    max_results: int = Query(default=5, ge=1, le=5),
) -> list[Source]:
    return search_web(
        query=query,
        subquestion="",
        max_results=max_results,
    )