from pydantic import BaseModel


class ScoutRequest(BaseModel):
    query: str


class ScoutResponse(BaseModel):
    query: str
    answer: str