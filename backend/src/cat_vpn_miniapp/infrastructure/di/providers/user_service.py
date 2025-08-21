from dishka import Provider, Scope, provide

from cat_vpn_miniapp.application.services.user_service import UserServiceImpl
from cat_vpn_miniapp.domain.interfaces.repositories import KeyRepository, UserRepository
from cat_vpn_miniapp.domain.interfaces.services import UserService
from cat_vpn_miniapp.domain.interfaces.transaction_manager import TransactionManager


class UserServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.REQUEST)
    async def get_repository(
            self, user_repo: UserRepository,
            key_repo: KeyRepository,
            t_manager: TransactionManager
    ) -> UserService:
        return UserServiceImpl(user_repo=user_repo, t_manager=t_manager, key_repo=key_repo)
