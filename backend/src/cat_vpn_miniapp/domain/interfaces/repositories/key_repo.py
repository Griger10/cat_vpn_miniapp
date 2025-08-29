from datetime import datetime
from typing import Protocol

from cat_vpn_miniapp.domain.models import VPNKey


class KeyRepository(Protocol):
    async def get_user_vpn_key(self, tid: int) -> VPNKey | None: ...

    async def add_key_for_user(self, tid: int, unique_key: str, valid_until: datetime) -> None: ...
