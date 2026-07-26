from datetime import date

from pydantic import BaseModel, ConfigDict


class ChargesheetDetailsSchema(BaseModel):
    CSID: int
    CaseMasterID: int
    csdate: date
    cstype: str
    PolicePersonID: int

    model_config = ConfigDict(from_attributes=True)