from app.database.models.occupation_master import Occupation
from app.repositories.base_repository import BaseRepository


class OccupationRepository(BaseRepository[Occupation]):
    def __init__(self):
        super().__init__(Occupation)


occupation_repository = OccupationRepository()