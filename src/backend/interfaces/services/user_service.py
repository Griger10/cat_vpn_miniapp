from typing import Protocol

from backend.models import User


class UserService(Protocol):
    async def get_user(self, tid: int) -> User | None: ...

    async def add_user(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None: ...
