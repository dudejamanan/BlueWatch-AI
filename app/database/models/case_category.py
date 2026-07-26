from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class CaseCategory(Base):
    __tablename__ = "case_categories"

    CaseCategoryID: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    LookupValue: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )