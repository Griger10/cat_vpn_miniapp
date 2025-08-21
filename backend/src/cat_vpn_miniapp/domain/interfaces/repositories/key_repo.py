from typing import Protocol

from cat_vpn_miniapp.domain.models import VPNKey


class KeyRepository(Protocol):

    async def get_user_vpn_key(self, tid: int) -> VPNKey | None: ...
