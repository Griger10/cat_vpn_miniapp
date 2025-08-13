from dishka import Provider

from backend.core.di.providers.bot import BotProvider
from backend.core.di.providers.config import ConfigProvider
from backend.core.di.providers.database import DatabaseProvider
from backend.core.di.providers.transaction_manager import TransactionManagerProvider
from backend.core.di.providers.user_repo import UserRepositoryProvider


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
        BotProvider(),
        UserRepositoryProvider(),
        TransactionManagerProvider(),
    ]
