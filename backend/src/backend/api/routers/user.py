from aiogram.utils.web_app import WebAppInitData
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.requests import Request
from prometheus_client import Counter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from backend.api.routers.dependencies import auth
from backend.interfaces import UserService

REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total number of HTTP requests for endpoints",
    ["method", "endpoint"]
)

user_router = APIRouter(
    prefix="/users",
    route_class=DishkaRoute,
    tags=["users"]
)


@user_router.get("/info/", status_code=HTTP_200_OK)
async def user_information(
        request: Request,
        user_service: FromDishka[UserService],
        auth_data: WebAppInitData = Depends(auth),
) -> JSONResponse:
    REQUESTS_TOTAL.labels(method="GET", endpoint="/info/").inc()
    await user_service.add_user_if_not_registered(
        tid=auth_data.user.id,
        first_name=auth_data.user.first_name,
        last_name=auth_data.user.last_name,
        username=auth_data.user.username,
    )
    user_info = await user_service.get_user(auth_data.user.id)
    key = user_info.key.unique_key if user_info.key else None
    valid_until = user_info.key.valid_until.strftime("%d.%m.%Y") if key and key.valid_until else None
    return JSONResponse(
        {
            "user_id": auth_data.user.id,
            "vpn_key": key,
            "vpn_key_expiry": valid_until
        }
    )
