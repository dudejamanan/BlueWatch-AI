from app.database.models.crime_head import CrimeHead
from app.repositories.base_repository import BaseRepository


class CrimeHeadRepository(BaseRepository[CrimeHead]):
    def __init__(self):
        super().__init__(CrimeHead)


crime_head_repository = CrimeHeadRepository()