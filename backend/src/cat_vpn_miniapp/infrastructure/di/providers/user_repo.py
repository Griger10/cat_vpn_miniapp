from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from cat_vpn_miniapp.interfaces import UserRepository
from cat_vpn_miniapp.repositories import UserRepositoryImpl


class UserRepositoryProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.REQUEST)
    async def get_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepositoryImpl(session)
