from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CrimeSubHead(Base):
    __tablename__ = "crime_sub_heads"

    CrimeSubHeadID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    CrimeHeadID: Mapped[int] = mapped_column(
        ForeignKey("crime_heads.CrimeHeadID"),
        nullable=False
    )

    CrimeHeadName: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    SeqID: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    crime_head = relationship(
        "CrimeHead",
        back_populates="sub_heads"
    )