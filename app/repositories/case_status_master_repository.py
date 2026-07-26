from app.database.models.case_status_master import CaseStatus
from app.repositories.base_repository import BaseRepository


class CaseStatusRepository(BaseRepository[CaseStatus]):
    def __init__(self):
        super().__init__(CaseStatus)


case_status_repository = CaseStatusRepository()