from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Court(Base):
    __tablename__ = "courts"

    CourtID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    CourtName: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    DistrictID: Mapped[int] = mapped_column(
        ForeignKey("District.DistrictID"),
        nullable=False,
    )

    StateID: Mapped[int] = mapped_column(
        ForeignKey("State.StateID"),
        nullable=False,
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    district = relationship("District")
    state = relationship("State")