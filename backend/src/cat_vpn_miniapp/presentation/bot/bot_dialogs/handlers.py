from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Button
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from cat_vpn_miniapp.application.services import UserService


async def select_user(
        callback: CallbackQuery,
        widget: Select,
        dialog_manager: DialogManager,
        item_id: str,
):
    dialog_manager.dialog_data["tid"] = int(item_id)
    await dialog_manager.next()


async def delete_message(
        callback: CallbackQuery,
        widget: Button,
        dialog_manager: DialogManager,
):
    await callback.message.delete()
    await dialog_manager.done()


async def process_key_for_user(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager,
):
    key = message.text.strip()
    dialog_manager.dialog_data["key"] = key
    await dialog_manager.next()

    

