from datetime import date

from pydantic import BaseModel, ConfigDict


class ArrestSurrenderBase(BaseModel):
    CaseMasterID: int
    ArrestSurrenderTypeID: int
    ArrestSurrenderDate: date
    ArrestSurrenderStateId: int
    ArrestSurrenderDistrictId: int
    PoliceStationID: int
    IOID: int
    CourtID: int
    AccusedMasterID: int
    IsAccused: bool
    IsComplainantAccused: bool


class ArrestSurrenderCreate(ArrestSurrenderBase):
    ArrestSurrenderID: int


class ArrestSurrenderUpdate(ArrestSurrenderBase):
    pass


class ArrestSurrenderResponse(ArrestSurrenderBase):
    ArrestSurrenderID: int

    model_config = ConfigDict(from_attributes=True)