from app.repositories.unit_type_repository import unit_type_repository
from app.services.base_service import BaseService


class UnitTypeService(BaseService):
    def __init__(self):
        super().__init__(unit_type_repository)


unit_type_service = UnitTypeService()