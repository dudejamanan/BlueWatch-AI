from app.repositories.rank_repository import rank_repository
from app.services.base_service import BaseService


class RankService(BaseService):
    def __init__(self):
        super().__init__(rank_repository)


rank_service = RankService()