from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Victim(Base):
    __tablename__ = "victims"

    VictimMasterID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    CaseMasterID: Mapped[int] = mapped_column(
        ForeignKey("case_masters.CaseMasterID"),
        nullable=False,
    )

    VictimName: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    AgeYear: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    GenderID: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    VictimPolice: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    case_master = relationship("CaseMaster")