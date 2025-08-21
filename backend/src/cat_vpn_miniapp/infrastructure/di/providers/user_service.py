from dishka import Provider, Scope, provide

from cat_vpn_miniapp.application.services.user_service import UserService
from cat_vpn_miniapp.application.transaction_manager import TransactionManager
from cat_vpn_miniapp.domain.interfaces import KeyRepository, UserRepository


class UserServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.REQUEST)
    async def get_repository(
            self, user_repo: UserRepository,
            key_repo: KeyRepository,
            t_manager: TransactionManager
    ) -> UserService:
        return UserService(user_repo=user_repo, t_manager=t_manager, key_repo=key_repo)
