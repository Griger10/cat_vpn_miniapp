from backend.interfaces import TransactionManager, UserRepository
from backend.models import User


class UserServiceImpl:
    def __init__(
            self,
            user_repo: UserRepository,
            t_manager: TransactionManager
    ) -> None:
        self.user_repo = user_repo
        self.t_manager = t_manager

    async def get_user(self, tid: int) -> User | None:
        return await self.user_repo.get_user_by_tid(tid)

    async def add_user(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None:
        await self.user_repo.upsert_user(tid, first_name, last_name, username)
        await self.t_manager.commit()
