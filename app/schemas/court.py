from pydantic import BaseModel, ConfigDict


class CourtBase(BaseModel):
    CourtName: str
    DistrictID: int
    StateID: int
    Active: bool


class CourtCreate(CourtBase):
    CourtID: int


class CourtUpdate(CourtBase):
    pass


class CourtResponse(CourtBase):
    CourtID: int

    model_config = ConfigDict(from_attributes=True)