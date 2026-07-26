from pydantic import BaseModel, ConfigDict


class OccupationBase(BaseModel):
    OccupationName: str


class OccupationCreate(OccupationBase):
    OccupationID: int


class OccupationUpdate(OccupationBase):
    pass


class OccupationResponse(OccupationBase):
    OccupationID: int

    model_config = ConfigDict(from_attributes=True)