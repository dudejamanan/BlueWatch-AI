from pydantic import BaseModel, ConfigDict


class VictimBase(BaseModel):
    CaseMasterID: int
    VictimName: str
    AgeYear: int
    GenderID: int
    VictimPolice: bool


class VictimCreate(VictimBase):
    VictimMasterID: int


class VictimUpdate(VictimBase):
    pass


class VictimResponse(VictimBase):
    VictimMasterID: int

    model_config = ConfigDict(from_attributes=True)