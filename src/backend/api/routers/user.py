from aiogram.utils.web_app import WebAppInitData
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.requests import Request
from starlette.responses import JSONResponse

from backend.api.routers.dependencies import auth
from backend.interfaces import UserService

user_router = APIRouter(
    prefix="/users",
    route_class=DishkaRoute,
    tags=["users"]
)


@user_router.get("/info/")
async def user_information(
        request: Request,
        user_service: FromDishka[UserService],
        auth_data: WebAppInitData = Depends(auth),
) -> JSONResponse:
    user_id = auth_data.user.id
    user_info = await user_service.get_user(user_id)
    if user_info is None:
        await user_service.add_user(
            tid=user_id,
            first_name=auth_data.user.first_name,
            last_name=auth_data.user.last_name,
            username=auth_data.user.username,
        )
    key = user_info.key.unique_key if user_info.key else None
    valid_until = user_info.key.valid_until.strftime("%d.%m.%Y") if user_info.key else None
    return JSONResponse(
        {
            "user_id": user_id,
            "vpn_key": key,
            "vpn_key_expiry": valid_until
        }
    )
