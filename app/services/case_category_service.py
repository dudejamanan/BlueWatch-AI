from app.repositories.case_category_repository import case_category_repository
from app.services.base_service import BaseService


class CaseCategoryService(BaseService):
    def __init__(self):
        super().__init__(case_category_repository)


case_category_service = CaseCategoryService()