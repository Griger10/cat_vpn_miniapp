import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import Redis, RedisStorage
from dishka.integrations.aiogram import setup_dishka as setup_aiogram_dishka

from backend.bot.handlers import user_handlers
from backend.core.config import Config
from backend.core.di.ioc import create_container
from backend.core.logging import configure_logging

configure_logging()

logger = logging.getLogger(__name__)


async def main() -> None:
    container = create_container()

    config = Config()

    redis = Redis(
        host=config.redis_config.host,
        port=config.redis_config.port,
    )

    storage = RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(
            with_destiny=True
        ),
    )

    bot = await container.get(Bot)

    dp = Dispatcher(storage=storage)

    dp.include_routers(
        user_handlers.router
    )

    setup_aiogram_dishka(container=container, router=dp, auto_inject=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
