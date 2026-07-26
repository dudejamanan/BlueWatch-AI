from app.repositories.occupation_master_repository import occupation_repository
from app.services.base_service import BaseService


class OccupationService(BaseService):
    def __init__(self):
        super().__init__(occupation_repository)


occupation_service = OccupationService()