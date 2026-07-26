from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Accused(Base):
    __tablename__ = "accused"

    AccusedMasterID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    CaseMasterID: Mapped[int] = mapped_column(
        ForeignKey("case_masters.CaseMasterID"),
        nullable=False,
    )

    AccusedName: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    AgeYear: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    GenderID: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    PersonID: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    case_master = relationship("CaseMaster")