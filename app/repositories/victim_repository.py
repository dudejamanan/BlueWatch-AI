from app.database.models.victim import Victim
from app.repositories.base_repository import BaseRepository


class VictimRepository(BaseRepository[Victim]):
    def __init__(self):
        super().__init__(Victim)


victim_repository = VictimRepository()