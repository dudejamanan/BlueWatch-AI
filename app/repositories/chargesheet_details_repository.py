from app.database.models.chargesheet_details import ChargesheetDetails
from app.repositories.base_repository import BaseRepository


class ChargesheetDetailsRepository(BaseRepository):
    def __init__(self):
        super().__init__(ChargesheetDetails)


chargesheet_details_repository = ChargesheetDetailsRepository()