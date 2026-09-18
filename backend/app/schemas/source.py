from pydantic import BaseModel


class Source(BaseModel):
    title: str
    url: str
    snippet: str
    provider: str
    search_query: str
    subquestion: str