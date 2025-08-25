from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from cat_vpn_miniapp.domain.models import User
from cat_vpn_miniapp.infrastructure.persistence import (
    SQLAlchemyUser,
    SQLAlchemyVPNKey,
)


def _to_domain_model(orm_model: SQLAlchemyUser) -> User | None:
    if orm_model is None:
        return None
    return User(
        tid=orm_model.tid,
        first_name=orm_model.first_name,
        last_name=orm_model.last_name,
        username=orm_model.username,
    )


class SQLAlchemyUserRepository:
    user: type[SQLAlchemyUser] = SQLAlchemyUser
    key: type[SQLAlchemyVPNKey] = SQLAlchemyVPNKey

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_by_tid(self, tid: int) -> User | None:
        stmt = select(self.user).where(self.user.tid == tid)

        result = await self._session.execute(stmt)

        return _to_domain_model(result.scalar_one_or_none())

    async def upsert_user(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None:
        stmt = insert(self.user).values(
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
        stmt = select(self.user).join(self.key, self.user.key).where(
            self.key.valid_until.isnot(None),
            self.key.valid_until >= datetime.now() - timedelta(days=1)
        )

        result = await self._session.execute(stmt)

        return [_to_domain_model(user) for user in result.scalars().all()]

    async def add_user_vpn_key(self, tid: int, key: str, valid_until: datetime) -> None:
        stmt = insert(self.key).values(
            tid=tid,
            unique_key=key,
            valid_until=valid_until,
        )

        await self._session.execute(stmt)
