from app.repositories.victim_repository import victim_repository
from app.services.base_service import BaseService


class VictimService(BaseService):
    def __init__(self):
        super().__init__(victim_repository)


victim_service = VictimService()