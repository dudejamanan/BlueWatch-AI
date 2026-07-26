from pydantic import BaseModel, ConfigDict


class GravityOffenceBase(BaseModel):
    LookupValue: str


class GravityOffenceCreate(GravityOffenceBase):
    GravityOffenceID: int


class GravityOffenceUpdate(GravityOffenceBase):
    pass


class GravityOffenceResponse(GravityOffenceBase):
    GravityOffenceID: int

    model_config = ConfigDict(from_attributes=True)