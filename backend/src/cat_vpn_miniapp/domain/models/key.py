from dataclasses import dataclass
from datetime import datetime


@dataclass
class VPNKey:
    vpn_key_id: int
    unique_key: str
    valid_until: datetime | None
    tid: int
