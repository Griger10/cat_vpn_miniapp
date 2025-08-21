from fastapi import APIRouter
from fastapi.responses import Response
from prometheus_client import generate_latest

metrics_router = APIRouter(
    tags=["metrics"]
)

@metrics_router.get("/metrics")
async def get_metrics():
    return Response(
        content=generate_latest(),
        media_type="text/plain; version=0.0.4; charset=utf-8"
    )
