from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Complainant(Base):
    __tablename__ = "complainants"

    ComplainantID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )

    CaseMasterID: Mapped[int] = mapped_column(
        ForeignKey("case_masters.CaseMasterID"),
        nullable=False,
    )

    ComplainantName: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    AgeYear: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    OccupationID: Mapped[int] = mapped_column(
        ForeignKey("occupations.OccupationID"),
        nullable=False,
    )

    ReligionID: Mapped[int] = mapped_column(
        ForeignKey("religions.ReligionID"),
        nullable=False,
    )

    CasteID: Mapped[int] = mapped_column(
        ForeignKey("castes.caste_master_id"),
        nullable=False,
    )
    GenderID: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    case_master = relationship("CaseMaster")
    occupation = relationship("Occupation")
    religion = relationship("Religion")
    caste = relationship("Caste")