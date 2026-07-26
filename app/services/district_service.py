from sqlalchemy.orm import Session

from app.repositories.district_repository import district_repository
from app.services.base_service import BaseService


class DistrictService(BaseService):
    def __init__(self):
        super().__init__(district_repository)

    def get_by_state(self, db: Session, state_id: int):
        return self.repository.get_by_state(db, state_id)


district_service = DistrictService()