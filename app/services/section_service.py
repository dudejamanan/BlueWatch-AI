from app.repositories.section_repository import section_repository
from app.services.base_service import BaseService


class SectionService(BaseService):
    def __init__(self):
        super().__init__(section_repository)


section_service = SectionService()