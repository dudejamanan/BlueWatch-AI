from sqlalchemy.orm import Session

from app.repositories.unit_repository import unit_repository
from app.services.base_service import BaseService


class UnitService(BaseService):
    def __init__(self):
        super().__init__(unit_repository)

    def get_by_district(self, db: Session, district_id: int):
        return self.repository.get_by_district(db, district_id)


unit_service = UnitService()