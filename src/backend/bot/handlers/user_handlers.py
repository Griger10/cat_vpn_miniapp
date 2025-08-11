from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from dishka import FromDishka

from backend.bot.keyboards.main_menu import set_main_menu
from backend.bot.keyboards.user_keyboards import get_main_keyboard
from backend.core.config import Config

router = Router()


@router.message(Command(commands=["start", "menu"]))
async def start(message: Message, bot: Bot, config: FromDishka[Config]):
    await set_main_menu(bot)

    keyboard = get_main_keyboard(
        admin_url=config.bot_config.admin_url,
        web_app_url=config.bot_config.web_app_url,
    )
    await message.answer("<b>🏠 Главное меню</b>", reply_markup=keyboard)
