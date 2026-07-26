from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.state import State


class StateRepository:

    @staticmethod
    def get_all(db: Session):
        return db.scalars(select(State)).all()