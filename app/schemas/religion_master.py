from pydantic import BaseModel, ConfigDict


class ReligionBase(BaseModel):
    ReligionName: str


class ReligionCreate(ReligionBase):
    ReligionID: int


class ReligionUpdate(ReligionBase):
    pass


class ReligionResponse(ReligionBase):
    ReligionID: int

    model_config = ConfigDict(from_attributes=True)