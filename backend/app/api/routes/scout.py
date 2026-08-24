from fastapi import APIRouter

from app.schemas.scout import ScoutRequest, ScoutResponse
from app.services.scout_service import run_scout


router = APIRouter()


@router.post("/scout", response_model=ScoutResponse)
def scout(request: ScoutRequest):
    return run_scout(request.query)