from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ArrestSurrender(Base):
    __tablename__ = "arrest_surrenders"

    ArrestSurrenderID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    CaseMasterID: Mapped[int] = mapped_column(
        ForeignKey("case_masters.CaseMasterID"),
        nullable=False,
    )

    ArrestSurrenderTypeID: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    ArrestSurrenderDate: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    ArrestSurrenderStateId: Mapped[int] = mapped_column(
        ForeignKey("State.StateID"),
        nullable=False,
    )

    ArrestSurrenderDistrictId: Mapped[int] = mapped_column(
        ForeignKey("District.DistrictID"),
        nullable=False,
    )

    PoliceStationID: Mapped[int] = mapped_column(
        ForeignKey("Unit.UnitID"),
        nullable=False,
    )

    IOID: Mapped[int] = mapped_column(
        ForeignKey("Employee.EmployeeID"),
        nullable=False,
    )

    CourtID: Mapped[int] = mapped_column(
        ForeignKey("courts.CourtID"),
        nullable=False,
    )

    AccusedMasterID: Mapped[int] = mapped_column(
        ForeignKey("accused.AccusedMasterID"),
        nullable=False,
    )

    IsAccused: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    IsComplainantAccused: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    case_master = relationship("CaseMaster")
    state = relationship("State")
    district = relationship("District")
    police_station = relationship("Unit")
    investigating_officer = relationship("Employee")
    court = relationship("Court")
    accused = relationship("Accused")