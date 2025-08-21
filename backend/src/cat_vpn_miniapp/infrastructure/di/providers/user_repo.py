from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from cat_vpn_miniapp.domain.interfaces.repositories import UserRepository
from cat_vpn_miniapp.infrastructure.persistence.sqlalchemy.repositories import SQLAlchemyUserRepository


class UserRepositoryProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.REQUEST)
    async def get_repository(self, session: AsyncSession) -> UserRepository:
        return SQLAlchemyUserRepository(session)
