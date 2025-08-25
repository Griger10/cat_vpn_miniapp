from cat_vpn_miniapp.application.transaction_manager import TransactionManager
from cat_vpn_miniapp.domain.interfaces import KeyRepository, UserRepository
from cat_vpn_miniapp.domain.models import User, VPNKey


class UserService:
    def __init__(
            self,
            user_repo: UserRepository,
            t_manager: TransactionManager,
            key_repo: KeyRepository,
    ) -> None:
        self.user_repo = user_repo
        self.t_manager = t_manager
        self.key_repo = key_repo

    async def get_user(self, tid: int) -> User | None:
        return await self.user_repo.get_user_by_tid(tid)

    async def add_user_if_not_registered(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None:
        await self.user_repo.upsert_user(tid, first_name, last_name, username)
        await self.t_manager.commit()

    async def get_users_with_expiring_keys(self) -> list[User] | None:
        return await self.user_repo.get_users_with_expiring_keys()

    async def get_user_vpn_key(self, tid: int) -> VPNKey | None:
        return await self.key_repo.get_user_vpn_key(tid)

    async def add_user_vpn_key(self, tid: int, key: str) -> None:
        await self.user_repo.add_user_vpn_key(tid, key)
        await self.t_manager.commit()
