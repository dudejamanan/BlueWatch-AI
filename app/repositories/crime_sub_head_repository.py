from app.database.models.crime_sub_head import CrimeSubHead
from app.repositories.base_repository import BaseRepository


class CrimeSubHeadRepository(BaseRepository[CrimeSubHead]):
    def __init__(self):
        super().__init__(CrimeSubHead)


crime_sub_head_repository = CrimeSubHeadRepository()