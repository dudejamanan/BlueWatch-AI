from app.database.models.case_master import CaseMaster
from app.repositories.base_repository import BaseRepository


class CaseMasterRepository(BaseRepository[CaseMaster]):
    def __init__(self):
        super().__init__(CaseMaster)


case_master_repository = CaseMasterRepository()