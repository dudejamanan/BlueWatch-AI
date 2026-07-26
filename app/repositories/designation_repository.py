from app.database.models.designation import Designation
from app.repositories.base_repository import BaseRepository


class DesignationRepository(BaseRepository[Designation]):
    def __init__(self):
        super().__init__(Designation)


designation_repository = DesignationRepository()