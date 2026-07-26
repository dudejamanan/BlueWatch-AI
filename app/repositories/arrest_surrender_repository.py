from app.database.models.arrest_surrender import ArrestSurrender
from app.repositories.base_repository import BaseRepository


class ArrestSurrenderRepository(BaseRepository[ArrestSurrender]):
    def __init__(self):
        super().__init__(ArrestSurrender)


arrest_surrender_repository = ArrestSurrenderRepository()