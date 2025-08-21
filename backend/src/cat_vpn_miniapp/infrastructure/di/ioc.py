from dishka import AsyncContainer, make_async_container

from cat_vpn_miniapp.domain.config import Config
from cat_vpn_miniapp.infrastructure.di.providers import get_providers


def create_container() -> AsyncContainer:
    context = {
        Config: Config(),
    }
    container = make_async_container(*get_providers(), context=context)

    return container
