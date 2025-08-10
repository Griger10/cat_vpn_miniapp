from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, relationship, mapped_column

from backend.core.db import Base


class User(Base):
    __tablename__ = "users"

    tid: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]

    keys: Mapped[list["VPNKey"]] = relationship("VPNKey", back_populates="user")
