from app.repositories.gravity_offence_repository import gravity_offence_repository
from app.services.base_service import BaseService


class GravityOffenceService(BaseService):
    def __init__(self):
        super().__init__(gravity_offence_repository)


gravity_offence_service = GravityOffenceService()