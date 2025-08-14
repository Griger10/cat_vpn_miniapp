from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from backend.core.db import Base


class VPNKey(Base):
    __tablename__ = "keys"

    vpn_key_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(unique=True)
    valid_until: Mapped[datetime | None]
    tid: Mapped[int] = mapped_column(
        ForeignKey("users.tid", ondelete="CASCADE", onupdate="CASCADE"),
    )

    user = relationship("User", back_populates="keys")
