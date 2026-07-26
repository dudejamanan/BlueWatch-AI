from pydantic import BaseModel, ConfigDict


class AccusedBase(BaseModel):
    CaseMasterID: int
    AccusedName: str
    AgeYear: int
    GenderID: str
    PersonID: str


class AccusedCreate(AccusedBase):
    AccusedMasterID: int


class AccusedUpdate(AccusedBase):
    pass


class AccusedResponse(AccusedBase):
    AccusedMasterID: int

    model_config = ConfigDict(from_attributes=True)