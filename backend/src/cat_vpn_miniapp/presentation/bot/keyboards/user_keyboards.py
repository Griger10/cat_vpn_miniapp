from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_keyboard(web_app_url: str, admin_url: str) -> InlineKeyboardMarkup:
    web_app = WebAppInfo(url=web_app_url)
    return (
        InlineKeyboardBuilder()
        .button(text="⚙️ Настроить VPN", web_app=web_app)
        .button(text="❓ Техподдержка", url=admin_url)
        .adjust(1)
        .as_markup()
    )


def get_admin_main_keyboard(web_app_url: str, admin_url: str):
    web_app = WebAppInfo(url=web_app_url)
    return (
        InlineKeyboardBuilder()
        .button(text="⚙️ Настроить VPN", web_app=web_app)
        .button(text="❓ Техподдержка", url=admin_url)
        .button(text="🔑 Выдать ключ", callback_data="give_key")
        .adjust(1)
        .as_markup()
    )
