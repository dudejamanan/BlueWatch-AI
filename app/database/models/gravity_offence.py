from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class GravityOffence(Base):
    __tablename__ = "gravity_offences"

    GravityOffenceID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    LookupValue: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )