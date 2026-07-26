from app.repositories.court_repository import court_repository
from app.services.base_service import BaseService


class CourtService(BaseService):
    def __init__(self):
        super().__init__(court_repository)


court_service = CourtService()