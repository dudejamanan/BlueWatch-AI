from app.repositories.crime_head_act_section_repository import (
    crime_head_act_section_repository,
)
from app.services.base_service import BaseService


class CrimeHeadActSectionService(BaseService):
    def __init__(self):
        super().__init__(crime_head_act_section_repository)


crime_head_act_section_service = CrimeHeadActSectionService()