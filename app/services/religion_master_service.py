from app.repositories.religion_master_repository import religion_repository
from app.services.base_service import BaseService


class ReligionService(BaseService):
    def __init__(self):
        super().__init__(religion_repository)


religion_service = ReligionService()