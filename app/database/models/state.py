from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

from sqlalchemy.orm import relationship

class State(Base):
    __tablename__ = "State"

    StateID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    StateName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    NationalityID: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    Active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    districts = relationship(
    "District",
    back_populates="state"
    )
    units = relationship("Unit")