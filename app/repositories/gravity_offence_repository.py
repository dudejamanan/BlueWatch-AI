from app.database.models.gravity_offence import GravityOffence
from app.repositories.base_repository import BaseRepository


class GravityOffenceRepository(BaseRepository[GravityOffence]):
    def __init__(self):
        super().__init__(GravityOffence)


gravity_offence_repository = GravityOffenceRepository()