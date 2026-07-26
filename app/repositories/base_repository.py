from typing import Generic, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from sqlalchemy import select

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model


    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.scalars(
            select(self.model)
            .offset(skip)
            .limit(limit)
        ).all()

    def get_by_id(self, db: Session, id_value, id_column):
        return db.scalar(
            select(self.model).where(id_column == id_value)
        )

    def create(self, db: Session, obj: T):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, obj: T):
        db.delete(obj)
        db.commit()