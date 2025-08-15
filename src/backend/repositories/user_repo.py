from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import User


class UserRepositoryImpl:
    model: type[User] = User

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_by_tid(self, tid: int) -> User | None:
        stmt = select(self.model).where(self.model.tid == tid)

        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def upsert_user(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None:
        stmt = insert(self.model).values(
            tid=tid,
            username=username,
            first_name=first_name,
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=["tid"],
            set_={
                "first_name": first_name,
                "last_name": last_name,
            },
        )

        await self._session.execute(stmt)
