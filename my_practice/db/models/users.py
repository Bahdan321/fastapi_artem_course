from db.base import Base

from datetime import datetime
from sqlalchemy import JSON, MetaData, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

metadata = MetaData()

class Roles(Base):

    metadata,
    name: Mapped[str] = mapped_column(nullable=False)
    premissions: Mapped[Optional[dict[list]]] = mapped_column(type_=JSON)

class Users(Base):

    metadata,
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[TIMESTAMP] = mapped_column(default=datetime.utcnow)
    role_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
