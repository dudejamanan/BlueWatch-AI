from app.repositories.designation_repository import designation_repository
from app.services.base_service import BaseService


class DesignationService(BaseService):
    def __init__(self):
        super().__init__(designation_repository)


designation_service = DesignationService()