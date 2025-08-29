from collections.abc import AsyncIterable

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import Provider, Scope, provide

from cat_vpn_miniapp.bootstrap.config import Config


class BotProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_bot(self, config: Config) -> AsyncIterable[Bot]:
        async with Bot(
            token=config.bot_config.token.get_secret_value(),
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML,
            ),
        ) as bot:
            yield bot
