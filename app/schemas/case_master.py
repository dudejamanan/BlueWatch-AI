from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class CaseMasterBase(BaseModel):
    CrimeNo: str
    CaseNo: str
    CrimeRegisteredDate: date

    PolicePersonID: int
    PoliceStationID: int

    CaseCategoryID: int
    GravityOffenceID: int

    CrimeMajorHeadID: int
    CrimeMinorHeadID: int

    CaseStatusID: int
    CourtID: int | None = None

    IncidentFromDate: datetime
    IncidentToDate: datetime
    InfoReceivedPSDate: datetime

    latitude: float
    longitude: float

    BriefFacts: str


class CaseMasterCreate(CaseMasterBase):
    CaseMasterID: int


class CaseMasterUpdate(CaseMasterBase):
    pass


class CaseMasterResponse(CaseMasterBase):
    CaseMasterID: int

    model_config = ConfigDict(from_attributes=True)