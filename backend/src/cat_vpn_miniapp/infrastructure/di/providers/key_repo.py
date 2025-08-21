from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from cat_vpn_miniapp.domain.interfaces.repositories import KeyRepository
from cat_vpn_miniapp.infrastructure.persistence.sqlalchemy.repositories import SQLAlchemyKeyRepository


class KeyRepositoryProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_key_repo(self, session: AsyncSession) -> KeyRepository:
        return SQLAlchemyKeyRepository(session)
