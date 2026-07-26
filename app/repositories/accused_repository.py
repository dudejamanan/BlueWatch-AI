from app.database.models.accused import Accused
from app.repositories.base_repository import BaseRepository


class AccusedRepository(BaseRepository[Accused]):
    def __init__(self):
        super().__init__(Accused)


accused_repository = AccusedRepository()