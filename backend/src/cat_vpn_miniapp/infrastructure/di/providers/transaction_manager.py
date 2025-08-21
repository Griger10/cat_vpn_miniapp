from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from cat_vpn_miniapp.application.transaction_manager import TransactionManagerImpl
from cat_vpn_miniapp.domain.interfaces.transaction_manager import TransactionManager


class TransactionManagerProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.REQUEST)
    async def get_repository(self, session: AsyncSession) -> TransactionManager:
        return TransactionManagerImpl(session)
