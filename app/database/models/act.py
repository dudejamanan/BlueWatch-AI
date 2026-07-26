from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Act(Base):
    __tablename__ = "acts"

    ActCode: Mapped[str] = mapped_column(
        String(20),
        primary_key=True
    )

    ActDescription: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    ShortName: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    sections = relationship(
        "Section",
        back_populates="act",
        cascade="all, delete-orphan"
    )