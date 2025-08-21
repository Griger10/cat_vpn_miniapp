from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    bot_commands = [
        BotCommand(command="/menu", description="Главное меню"),
    ]

    await bot.set_my_commands(bot_commands)
