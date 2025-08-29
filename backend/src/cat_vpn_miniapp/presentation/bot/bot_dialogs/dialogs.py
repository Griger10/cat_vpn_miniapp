from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Const, Format

from cat_vpn_miniapp.presentation.bot.bot_dialogs.getters import get_all_users
from cat_vpn_miniapp.presentation.bot.bot_dialogs.handlers import (
    delete_message,
    process_key_for_user,
    select_user,
    set_key_for_user,
)
from cat_vpn_miniapp.presentation.bot.fsm import AddKeyFSM
from cat_vpn_miniapp.presentation.bot.keyboards.customized_calendar import CustomCalendar
from cat_vpn_miniapp.presentation.bot.utils.dialogs import go_back

add_key_dialog = Dialog(
    Window(
        Const("<b>Выберите пользователя:</b>"),
        ScrollingGroup(
            Select(
                Format("{item.first_name} {item.last_name}"),
                items="users",
                item_id_getter=lambda user: user.tid,
                id="user_select",
                on_click=select_user,
            ),
            width=1,
            height=5,
            id="user_scrolling_group",
        ),
        getter=get_all_users,
        state=AddKeyFSM.user,
    ),
    Window(
        Const("<b>Введите ключ доступа:</b>"),
        MessageInput(func=process_key_for_user, content_types=ContentType.TEXT),
        Button(text=Const("Назад"), on_click=go_back, id="go_back"),
        state=AddKeyFSM.key,
    ),
    Window(
        Const("<b>До какой даты ключ активен?</b>"),
        CustomCalendar(
            id="valid_until_select",
            on_click=set_key_for_user,
        ),
        Button(text=Const("Назад"), on_click=go_back, id="go_back"),
        state=AddKeyFSM.valid_until,
    ),
    Window(
        Const("<b>Отлично! Ключ доступа успешно выдан!</b>"),
        Button(text=Const("Закрыть"), on_click=delete_message, id="delete_message"),
        state=AddKeyFSM.success,
    ),
)
