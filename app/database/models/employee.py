from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Employee(Base):
    __tablename__ = "Employee"

    EmployeeID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    DistrictID: Mapped[int] = mapped_column(
        ForeignKey("District.DistrictID"),
        nullable=False,
    )

    UnitID: Mapped[int] = mapped_column(
        ForeignKey("Unit.UnitID"),
        nullable=False,
    )

    RankID: Mapped[int] = mapped_column(
        ForeignKey("Rank.RankID"),
        nullable=False,
    )

    DesignationID: Mapped[int] = mapped_column(
        ForeignKey("Designation.DesignationID"),
        nullable=False,
    )

    KGID: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    FirstName: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    EmployeeDOB: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    GenderID: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    BloodGroupID: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    PhysicallyChallenged: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    AppointmentDate: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    district = relationship("District")
    unit = relationship("Unit")
    rank = relationship("Rank", back_populates="employees")
    designation = relationship("Designation", back_populates="employees")