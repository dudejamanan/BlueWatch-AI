from app.repositories.arrest_surrender_repository import (
    arrest_surrender_repository,
)
from app.services.base_service import BaseService


class ArrestSurrenderService(BaseService):
    def __init__(self):
        super().__init__(arrest_surrender_repository)


arrest_surrender_service = ArrestSurrenderService()