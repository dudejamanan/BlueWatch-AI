from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Designation(Base):
    __tablename__ = "Designation"

    DesignationID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    DesignationName: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    SortOrder: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    employees = relationship("Employee", back_populates="designation")