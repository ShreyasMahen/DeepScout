from fastapi import FastAPI

app = FastAPI(
    title="DeepScout API",
    description="Backend API for the DeepScout AI Research Engine",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "DeepScout API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }