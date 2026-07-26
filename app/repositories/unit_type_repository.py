from app.database.models.unit_type import UnitType
from app.repositories.base_repository import BaseRepository


class UnitTypeRepository(BaseRepository[UnitType]):
    def __init__(self):
        super().__init__(UnitType)


unit_type_repository = UnitTypeRepository()