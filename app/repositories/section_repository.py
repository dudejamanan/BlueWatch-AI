from app.database.models.section import Section
from app.repositories.base_repository import BaseRepository


class SectionRepository(BaseRepository[Section]):
    def __init__(self):
        super().__init__(Section)


section_repository = SectionRepository()