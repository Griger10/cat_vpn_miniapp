from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button


async def go_next(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.next()


async def go_back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.back(show_mode=ShowMode.EDIT)


async def go_back_delete_and_send(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.back(show_mode=ShowMode.DELETE_AND_SEND)


async def do_nothing(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await callback.answer()


async def switch_to_previous_dialog(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.done(show_mode=ShowMode.EDIT)
