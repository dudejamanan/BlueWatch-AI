from app.database.models.court import Court
from app.repositories.base_repository import BaseRepository


class CourtRepository(BaseRepository[Court]):
    def __init__(self):
        super().__init__(Court)


court_repository = CourtRepository()