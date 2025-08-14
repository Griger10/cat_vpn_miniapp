from aiogram.utils.web_app import WebAppInitData
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.requests import Request
from starlette.responses import JSONResponse

from backend.api.routers.dependencies import auth

user_router = APIRouter(
    prefix="/users",
    route_class=DishkaRoute,
    tags=["users"]
)

@router.get("/info/")
async def user_info(
        request: Request,
        auth_data: WebAppInitData = Depends(auth)
) -> JSONResponse:
    user_id = auth_data.user.id
