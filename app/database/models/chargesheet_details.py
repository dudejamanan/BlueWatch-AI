from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ChargesheetDetails(Base):
    __tablename__ = "chargesheet_details"

    CSID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    CaseMasterID: Mapped[int] = mapped_column(
        ForeignKey("case_masters.CaseMasterID"),
        nullable=False,
    )

    csdate: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    cstype: Mapped[str] = mapped_column(
        String(1),
        nullable=False,
    )

    PolicePersonID: Mapped[int] = mapped_column(
        ForeignKey("Employee.EmployeeID"),
        nullable=False,
    )

    case_master = relationship("CaseMaster")
    police_person = relationship("Employee")