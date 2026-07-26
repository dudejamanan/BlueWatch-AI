from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Unit(Base):
    __tablename__ = "Unit"

    UnitID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    UnitName: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    TypeID: Mapped[int] = mapped_column(
        ForeignKey("UnitType.UnitTypeID"),
        nullable=False
    )

    ParentUnit: Mapped[int | None] = mapped_column(
        ForeignKey("Unit.UnitID"),
        nullable=True
    )

    NationalityID: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    StateID: Mapped[int] = mapped_column(
        ForeignKey("State.StateID"),
        nullable=False
    )

    DistrictID: Mapped[int] = mapped_column(
        ForeignKey("District.DistrictID"),
        nullable=False
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    unit_type = relationship("UnitType", back_populates="units")
    state = relationship("State")
    district = relationship("District")

    parent = relationship(
        "Unit",
        remote_side=[UnitID],
        back_populates="children"
    )

    children = relationship(
        "Unit",
        back_populates="parent"
    )