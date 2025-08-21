from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from dishka import FromDishka

from cat_vpn_miniapp.domain.config import Config
from cat_vpn_miniapp.presentation.bot.keyboards.main_menu import set_main_menu
from cat_vpn_miniapp.presentation.bot.keyboards.user_keyboards import get_main_keyboard

router = Router()


@router.message(Command(commands=["start", "menu"]))
async def start(message: Message, bot: Bot, config: FromDishka[Config]):
    await set_main_menu(bot)

    keyboard = get_main_keyboard(
        admin_url=config.bot_config.admin_url,
        web_app_url=config.bot_config.web_app_url,
    )
    await message.answer("<b>🏠 Главное меню</b>", reply_markup=keyboard)
