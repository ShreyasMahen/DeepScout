from openai import OpenAI

from app.core.config import settings
from app.schemas.scout import ScoutResponse


client = OpenAI(api_key=settings.openai_api_key)


def run_scout(query: str) -> ScoutResponse:
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=f"""
You are DeepScout, an AI research assistant.

Answer the following user query clearly and concisely:

{query}
"""
    )

    return ScoutResponse(
        query=query,
        answer=response.output_text
    )