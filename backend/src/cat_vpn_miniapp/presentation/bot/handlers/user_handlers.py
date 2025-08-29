from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from dishka import FromDishka

from cat_vpn_miniapp.bootstrap.config import Config
from cat_vpn_miniapp.presentation.bot.fsm import AddKeyFSM
from cat_vpn_miniapp.presentation.bot.keyboards.main_menu import set_main_menu
from cat_vpn_miniapp.presentation.bot.keyboards.user_keyboards import get_admin_main_keyboard, get_main_keyboard

router = Router()


@router.message(Command(commands=["start", "menu"]))
async def start(message: Message, bot: Bot, config: FromDishka[Config]):
    await set_main_menu(bot)
    if str(message.from_user.id) in config.bot_config.admin_ids:
        keyboard = get_admin_main_keyboard(
            admin_url=config.bot_config.admin_url,
            web_app_url=config.bot_config.web_app_url,
        )
    else:
        keyboard = get_main_keyboard(
            admin_url=config.bot_config.admin_url,
            web_app_url=config.bot_config.web_app_url,
        )
    await message.answer("<b>🏠 Главное меню</b>", reply_markup=keyboard)


@router.callback_query(F.data == "give_key")
async def start_give_key(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(AddKeyFSM.user)
    await callback.answer()
