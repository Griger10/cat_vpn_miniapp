import asyncio
import logging

import uvicorn
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import Redis, RedisStorage
from dishka.integrations.aiogram import setup_dishka as setup_aiogram_dishka
from dishka.integrations.fastapi import setup_dishka as setup_fastapi_dishka
from dishka.integrations.taskiq import setup_dishka as setup_taskiq_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from taskiq.api import run_receiver_task, run_scheduler_task

from backend.api.routers import user_router
from backend.bot.handlers import user_handlers
from backend.core.config import Config
from backend.core.logging import configure_logging
from backend.infrastructure.di.ioc import create_container
from backend.infrastructure.scheduler.broker import broker, scheduler
from backend.infrastructure.scheduler.tasks import process_users_with_expiring_keys  # noqa

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Кот MiniApp API",
    root_path="api",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)

container = create_container()
config = Config()

redis = Redis(
    host=config.redis_config.host,
    port=config.redis_config.port,
)

storage = RedisStorage(
    redis=redis,
    key_builder=DefaultKeyBuilder(with_destiny=True),
)

dp = Dispatcher(storage=storage)
dp.include_routers(user_handlers.router)

setup_aiogram_dishka(container=container, router=dp, auto_inject=True)
setup_fastapi_dishka(container=container, app=app)
setup_taskiq_dishka(container=container, broker=broker)


async def run_bot() -> None:
    bot = await container.get(Bot)
    logger.info("Starting Telegram bot...")
    await dp.start_polling(bot)
    logger.info("Telegram bot stopped")


async def run_api() -> None:
    server_config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=8000,
        log_level=logging.getLevelName(logging.INFO).lower()
    )
    server = uvicorn.Server(server_config)
    logger.info("Starting API server...")
    await server.serve()
    logger.info("API server stopped")


async def main():
    tasks = [
        asyncio.create_task(broker.startup()),
        asyncio.create_task(run_receiver_task(broker)),
        asyncio.create_task(run_scheduler_task(scheduler)),
        asyncio.create_task(run_bot()),
        asyncio.create_task(run_api()),
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
    except Exception as e:
        logger.exception(f"Application crashed: {e}")
