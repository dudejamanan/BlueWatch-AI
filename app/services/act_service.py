from app.repositories.act_repository import act_repository
from app.services.base_service import BaseService


class ActService(BaseService):
    def __init__(self):
        super().__init__(act_repository)


act_service = ActService()