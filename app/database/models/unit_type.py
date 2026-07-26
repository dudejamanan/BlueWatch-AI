from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class UnitType(Base):
    __tablename__ = "UnitType"

    UnitTypeID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    UnitTypeName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    units = relationship("Unit", back_populates="unit_type")