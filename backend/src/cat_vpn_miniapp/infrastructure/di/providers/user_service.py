from dishka import Provider, Scope, provide

from cat_vpn_miniapp.interfaces import TransactionManager, UserRepository, UserService
from cat_vpn_miniapp.services import UserServiceImpl


class UserServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.REQUEST)
    async def get_repository(
            self, user_repo: UserRepository, t_manager: TransactionManager
    ) -> UserService:
        return UserServiceImpl(user_repo=user_repo, t_manager=t_manager)
