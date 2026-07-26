

from app.database.models.religion_master import Religion
from app.repositories.base_repository import BaseRepository


class ReligionRepository(BaseRepository[Religion]):
    def __init__(self):
        super().__init__(Religion)


religion_repository = ReligionRepository()