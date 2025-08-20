from dishka import AsyncContainer, make_async_container

from backend.core.config import Config
from backend.infrastructure.di.providers import get_providers


def create_container() -> AsyncContainer:
    context = {
        Config: Config(),
    }
    container = make_async_container(*get_providers(), context=context)

    return container
