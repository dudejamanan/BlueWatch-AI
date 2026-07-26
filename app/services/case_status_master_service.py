from app.repositories.case_status_master_repository import (
    case_status_repository,
)
from app.services.base_service import BaseService


class CaseStatusService(BaseService):
    def __init__(self):
        super().__init__(case_status_repository)


case_status_service = CaseStatusService()