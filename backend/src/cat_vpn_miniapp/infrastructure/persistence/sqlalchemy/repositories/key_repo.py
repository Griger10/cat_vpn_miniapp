from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from cat_vpn_miniapp.domain.models import VPNKey
from cat_vpn_miniapp.infrastructure.persistence import SQLAlchemyUser, SQLAlchemyVPNKey


def _to_domain_model(orm_model: SQLAlchemyVPNKey) -> VPNKey | None:
    if orm_model is None:
        return None
    return VPNKey(
        vpn_key_id=orm_model.vpn_key_id,
        tid=orm_model.tid,
        unique_key=orm_model.unique_key,
        valid_until=orm_model.valid_until,
    )


class SQLAlchemyKeyRepository:
    key: type[SQLAlchemyVPNKey] = SQLAlchemyVPNKey
    user: type[SQLAlchemyUser] = SQLAlchemyUser

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_vpn_key(self, tid: int) -> VPNKey | None:
        stmt = select(self.key).join(self.user).where(
            self.user.tid == tid
        )

        result = await self._session.execute(stmt)

        return _to_domain_model(result.scalar_one_or_none())
