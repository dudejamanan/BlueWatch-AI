from app.database.models.crime_head_act_section import CrimeHeadActSection
from app.repositories.base_repository import BaseRepository


class CrimeHeadActSectionRepository(BaseRepository[CrimeHeadActSection]):
    def __init__(self):
        super().__init__(CrimeHeadActSection)


crime_head_act_section_repository = CrimeHeadActSectionRepository()