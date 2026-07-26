from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CrimeHead(Base):
    __tablename__ = "crime_heads"

    CrimeHeadID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    CrimeGroupName: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    sub_heads = relationship(
        "CrimeSubHead",
        back_populates="crime_head",
        cascade="all, delete-orphan"
    )

    act_sections = relationship(
        "CrimeHeadActSection",
        back_populates="crime_head",
        cascade="all, delete-orphan"
    )