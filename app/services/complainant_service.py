from app.repositories.complainant_repository import complainant_repository
from app.services.base_service import BaseService


class ComplainantService(BaseService):
    def __init__(self):
        super().__init__(complainant_repository)


complainant_service = ComplainantService()