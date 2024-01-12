from db.base import Base

from datetime import datetime
from sqlalchemy import JSON, MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),


)

class Roles(Base):

    metadata,
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    premissions: Mapped[JSON]

class Users(Base):

    metadata,
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[TIMESTAMP] = mapped_column(default=datetime.utcnow)
    role_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
