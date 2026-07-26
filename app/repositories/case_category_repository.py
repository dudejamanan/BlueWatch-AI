from app.database.models.case_category import CaseCategory
from app.repositories.base_repository import BaseRepository


class CaseCategoryRepository(BaseRepository[CaseCategory]):
    def __init__(self):
        super().__init__(CaseCategory)


case_category_repository = CaseCategoryRepository()