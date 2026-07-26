from app.repositories.crime_sub_head_repository import crime_sub_head_repository
from app.services.base_service import BaseService


class CrimeSubHeadService(BaseService):
    def __init__(self):
        super().__init__(crime_sub_head_repository)


crime_sub_head_service = CrimeSubHeadService()