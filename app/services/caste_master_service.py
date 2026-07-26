from app.repositories.caste_master_repository import caste_repository
from app.services.base_service import BaseService


class CasteService(BaseService):
    def __init__(self):
        super().__init__(caste_repository)


caste_service = CasteService()