from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from cachetools import TTLCache

from backend.repositories import TransactionManagerImpl, UserRepositoryImpl
from backend.services.user_service import UserServiceImpl

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.cache = TTLCache(
            maxsize=1000,
            ttl=60 * 60 * 24,
        )

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id

        if user_id not in self.cache:
            session: AsyncSession = data["session"]
            user_repo = UserRepositoryImpl(session)
            t_manager = TransactionManagerImpl(session)
            user_service = UserServiceImpl(
                user_repo=user_repo,
                t_manager=t_manager
            )

            await user_service.add_user(
                tid=event.from_user.id,
                username=event.from_user.username,
                first_name=event.from_user.first_name,
                last_name=event.from_user.last_name,
            )
            self.cache[user_id] = None
        return await handler(event, data)
