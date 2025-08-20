from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from backend.infrastructure.persistence import User, VPNKey


class UserRepositoryImpl:
    model: type[User] = User
    key: type[VPNKey] = VPNKey

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

    async def get_users_with_expiring_keys(self) -> list[User] | None:
        stmt = select(self.model).join(self.key, self.model.key).where(
            self.key.valid_until.isnot(None),
            self.key.valid_until >= datetime.now() - timedelta(days=1)
        )

        result = await self._session.execute(stmt)

        return list(result.scalars().all())
