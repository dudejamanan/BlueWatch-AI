from app.database.models.caste_master import Caste
from app.repositories.base_repository import BaseRepository


class CasteRepository(BaseRepository[Caste]):
    def __init__(self):
        super().__init__(Caste)


caste_repository = CasteRepository()