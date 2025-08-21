from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from cat_vpn_miniapp.infrastructure.persistence.sqlalchemy.db import Base


class SQLAlchemyVPNKey(Base):
    __tablename__ = "keys"

    vpn_key_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    unique_key: Mapped[str] = mapped_column(unique=True)
    valid_until: Mapped[datetime | None]
    tid: Mapped[int] = mapped_column(
        ForeignKey("users.tid", ondelete="CASCADE", onupdate="CASCADE"),
    )

    user = relationship("SQLAlchemyUser", back_populates="key")
