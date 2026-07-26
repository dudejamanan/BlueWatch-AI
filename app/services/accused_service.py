from app.repositories.accused_repository import accused_repository
from app.services.base_service import BaseService


class AccusedService(BaseService):
    def __init__(self):
        super().__init__(accused_repository)


accused_service = AccusedService()