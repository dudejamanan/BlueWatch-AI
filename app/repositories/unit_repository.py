from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.unit import Unit
from app.repositories.base_repository import BaseRepository


class UnitRepository(BaseRepository[Unit]):
    def __init__(self):
        super().__init__(Unit)

    def get_by_district(self, db: Session, district_id: int):
        return db.scalars(
            select(Unit).where(Unit.DistrictID == district_id)
        ).all()


unit_repository = UnitRepository()