from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Religion(Base):
    __tablename__ = "religions"

    ReligionID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    ReligionName: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )