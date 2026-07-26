from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Caste(Base):
    __tablename__ = "castes"

    caste_master_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    caste_master_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )