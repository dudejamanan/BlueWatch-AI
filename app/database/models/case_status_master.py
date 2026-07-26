from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class CaseStatus(Base):
    __tablename__ = "case_statuses"

    CaseStatusID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    CaseStatusName: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )