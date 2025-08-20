from dishka import Provider

from backend.infrastructure.di.providers.bot import BotProvider
from backend.infrastructure.di.providers.config import ConfigProvider
from backend.infrastructure.di.providers.database import DatabaseProvider
from backend.infrastructure.di.providers.transaction_manager import TransactionManagerProvider
from backend.infrastructure.di.providers.translator import TranslatorProvider
from backend.infrastructure.di.providers.user_repo import UserRepositoryProvider
from backend.infrastructure.di.providers.user_service import UserServiceProvider


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
        BotProvider(),
        UserRepositoryProvider(),
        TransactionManagerProvider(),
        UserServiceProvider(),
        TranslatorProvider(),
    ]
