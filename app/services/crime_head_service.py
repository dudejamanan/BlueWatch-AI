from app.repositories.crime_head_repository import crime_head_repository
from app.services.base_service import BaseService


class CrimeHeadService(BaseService):
    def __init__(self):
        super().__init__(crime_head_repository)


crime_head_service = CrimeHeadService()