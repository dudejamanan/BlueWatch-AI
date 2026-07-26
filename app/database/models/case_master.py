from datetime import date, datetime

from sqlalchemy import (
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CaseMaster(Base):
    __tablename__ = "case_masters"

    CaseMasterID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    CrimeNo: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    CaseNo: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    CrimeRegisteredDate: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    PolicePersonID: Mapped[int] = mapped_column(
        ForeignKey("Employee.EmployeeID"),
        nullable=False,
    )

    PoliceStationID: Mapped[int] = mapped_column(
        ForeignKey("Unit.UnitID"),
        nullable=False,
    )

    CaseCategoryID: Mapped[int] = mapped_column(
        ForeignKey("case_categories.CaseCategoryID"),
        nullable=False,
    )

    GravityOffenceID: Mapped[int] = mapped_column(
        ForeignKey("gravity_offences.GravityOffenceID"),
        nullable=False,
    )

    CrimeMajorHeadID: Mapped[int] = mapped_column(
        ForeignKey("crime_heads.CrimeHeadID"),
        nullable=False,
    )

    CrimeMinorHeadID: Mapped[int] = mapped_column(
        ForeignKey("crime_sub_heads.CrimeSubHeadID"),
        nullable=False,
    )

    CaseStatusID: Mapped[int] = mapped_column(
        ForeignKey("case_statuses.CaseStatusID"),
        nullable=False,
    )

    CourtID: Mapped[int | None] = mapped_column(
        ForeignKey("courts.CourtID"),
        nullable=True,
    )

    IncidentFromDate: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    IncidentToDate: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    InfoReceivedPSDate: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    BriefFacts: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    employee = relationship("Employee")
    police_station = relationship("Unit")
    case_category = relationship("CaseCategory")
    gravity_offence = relationship("GravityOffence")
    crime_major_head = relationship("CrimeHead")
    crime_minor_head = relationship("CrimeSubHead")
    case_status = relationship("CaseStatus")
    court = relationship("Court")