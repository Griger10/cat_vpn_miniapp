from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from cat_vpn_miniapp.infrastructure.persistence.sqlalchemy.db import Base


class SQLAlchemyUser(Base):
    __tablename__ = "users"

    tid: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]

    key = relationship("SQLAlchemyVPNKey", back_populates="user", uselist=False, lazy="joined")
