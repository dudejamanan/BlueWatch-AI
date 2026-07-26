from app.database.models.rank import Rank
from app.repositories.base_repository import BaseRepository


class RankRepository(BaseRepository[Rank]):
    def __init__(self):
        super().__init__(Rank)


rank_repository = RankRepository()