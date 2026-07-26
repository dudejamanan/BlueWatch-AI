from app.database.models.act import Act
from app.repositories.base_repository import BaseRepository


class ActRepository(BaseRepository[Act]):
    def __init__(self):
        super().__init__(Act)


act_repository = ActRepository()