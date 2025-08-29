from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from cat_vpn_miniapp.application.services import UserService


@inject
async def get_all_users(user_service: FromDishka[UserService], **kwargs) -> dict:
    users = await user_service.get_all_users()

    for user in users:
        if not user.last_name:
            user.last_name = ""

    return {"users": users}
