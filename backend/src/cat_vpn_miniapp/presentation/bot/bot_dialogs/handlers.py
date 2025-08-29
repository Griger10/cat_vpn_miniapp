from datetime import date, datetime

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from cat_vpn_miniapp.application.services import UserService
from cat_vpn_miniapp.presentation.bot.keyboards.customized_calendar import CustomCalendar


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


@inject
async def set_key_for_user(
    callback: CallbackQuery,
    widget: CustomCalendar,
    dialog_manager: DialogManager,
    selected_date: date,
    user_service: FromDishka[UserService],
):
    tid = dialog_manager.dialog_data["tid"]
    key = dialog_manager.dialog_data["key"]
    valid_until = datetime(selected_date.year, selected_date.month, selected_date.day)
    await user_service.add_user_vpn_key(
        tid=tid,
        key=key,
        valid_until=valid_until,
    )
    await dialog_manager.next()
