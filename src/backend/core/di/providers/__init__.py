from dishka import Provider

from backend.core.di.providers.bot import BotProvider
from backend.core.di.providers.config import ConfigProvider
from backend.core.di.providers.database import DatabaseProvider


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
        BotProvider(),
    ]
