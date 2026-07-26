from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class District(Base):
    __tablename__ = "District"

    DistrictID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    DistrictName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    StateID: Mapped[int] = mapped_column(
        ForeignKey("State.StateID"),
        nullable=False
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    state = relationship(
        "State",
        back_populates="districts"
    )