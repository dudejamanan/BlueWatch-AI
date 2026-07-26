from app.repositories.case_master_repository import case_master_repository
from app.services.base_service import BaseService


class CaseMasterService(BaseService):
    def __init__(self):
        super().__init__(case_master_repository)


case_master_service = CaseMasterService()