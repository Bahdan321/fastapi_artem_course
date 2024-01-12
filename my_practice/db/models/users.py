from db.base import Base

import datetime
from sqlalchemy import JSON, MetaData, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
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
    registered_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    role_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
