from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Occupation(Base):
    __tablename__ = "occupations"

    OccupationID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    OccupationName: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )