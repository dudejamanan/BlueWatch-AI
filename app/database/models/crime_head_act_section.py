from sqlalchemy import ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CrimeHeadActSection(Base):
    __tablename__ = "crime_head_act_sections"

    CrimeHeadID: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    ActCode: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    SectionCode: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    __table_args__ = (
        PrimaryKeyConstraint(
            "CrimeHeadID",
            "ActCode",
            "SectionCode"
        ),
        ForeignKeyConstraint(
            ["CrimeHeadID"],
            ["crime_heads.CrimeHeadID"]
        ),
        ForeignKeyConstraint(
            ["ActCode", "SectionCode"],
            ["sections.ActCode", "sections.SectionCode"]
        ),
    )

    crime_head = relationship(
        "CrimeHead",
        back_populates="act_sections"
    )

    section = relationship(
        "Section",
        back_populates="crime_head_links"
    )