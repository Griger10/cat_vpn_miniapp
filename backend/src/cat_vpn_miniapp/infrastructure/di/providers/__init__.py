from dishka import Provider

from cat_vpn_miniapp.infrastructure.di.providers.bot import BotProvider
from cat_vpn_miniapp.infrastructure.di.providers.config import ConfigProvider
from cat_vpn_miniapp.infrastructure.di.providers.database import DatabaseProvider
from cat_vpn_miniapp.infrastructure.di.providers.transaction_manager import TransactionManagerProvider
from cat_vpn_miniapp.infrastructure.di.providers.translator import TranslatorProvider
from cat_vpn_miniapp.infrastructure.di.providers.user_repo import UserRepositoryProvider
from cat_vpn_miniapp.infrastructure.di.providers.user_service import UserServiceProvider


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
