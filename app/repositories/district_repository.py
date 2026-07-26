from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.district import District
from app.repositories.base_repository import BaseRepository


class DistrictRepository(BaseRepository[District]):
    def __init__(self):
        super().__init__(District)

    def get_by_state(self, db: Session, state_id: int):
        return db.scalars(
            select(District).where(District.StateID == state_id)
        ).all()


district_repository = DistrictRepository()