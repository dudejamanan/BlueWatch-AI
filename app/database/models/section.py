from sqlalchemy import Boolean, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Section(Base):
    __tablename__ = "sections"

    ActCode: Mapped[str] = mapped_column(
        ForeignKey("acts.ActCode"),
        nullable=False
    )

    SectionCode: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    SectionDescription: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    __table_args__ = (
        PrimaryKeyConstraint(
            "ActCode",
            "SectionCode"
        ),
    )

    act = relationship(
        "Act",
        back_populates="sections"
    )

    crime_head_links = relationship(
        "CrimeHeadActSection",
        back_populates="section",
        cascade="all, delete-orphan"
    )