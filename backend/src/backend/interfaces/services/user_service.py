from typing import Protocol

from backend.infrastructure.persistence import User


class UserService(Protocol):
    async def get_user(self, tid: int) -> User | None: ...

    async def add_user_if_not_registered(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None: ...

    async def get_users_with_expiring_keys(self) -> list[User] | None: ...
