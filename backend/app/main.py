from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.scout import router as scout_router
from app.api.routes.planner import router as planner_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="Backend API for the DeepScout AI Research Engine",
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(scout_router)
app.include_router(planner_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
        "environment": settings.environment
    }