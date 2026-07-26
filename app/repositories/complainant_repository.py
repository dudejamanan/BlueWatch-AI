from app.database.models.complainant_details import Complainant
from app.repositories.base_repository import BaseRepository


class ComplainantRepository(BaseRepository[Complainant]):
    def __init__(self):
        super().__init__(Complainant)


complainant_repository = ComplainantRepository()