from app.repositories.chargesheet_details_repository import (
    chargesheet_details_repository,
)
from app.services.base_service import BaseService


class ChargesheetDetailsService(BaseService):
    def __init__(self):
        super().__init__(chargesheet_details_repository)


chargesheet_details_service = ChargesheetDetailsService()