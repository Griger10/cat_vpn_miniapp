from dishka import Provider

from cat_vpn_miniapp.bootstrap.di.providers.bot import BotProvider
from cat_vpn_miniapp.bootstrap.di.providers.config import ConfigProvider
from cat_vpn_miniapp.bootstrap.di.providers.database import DatabaseProvider
from cat_vpn_miniapp.bootstrap.di.providers.key_repo import KeyRepositoryProvider
from cat_vpn_miniapp.bootstrap.di.providers.transaction_manager import TransactionManagerProvider
from cat_vpn_miniapp.bootstrap.di.providers.translator import TranslatorProvider
from cat_vpn_miniapp.bootstrap.di.providers.user_repo import UserRepositoryProvider
from cat_vpn_miniapp.bootstrap.di.providers.user_service import UserServiceProvider


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
        BotProvider(),
        UserRepositoryProvider(),
        KeyRepositoryProvider(),
        TransactionManagerProvider(),
        UserServiceProvider(),
        TranslatorProvider(),
    ]
