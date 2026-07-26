from pydantic import BaseModel, ConfigDict


class CrimeHeadBase(BaseModel):
    CrimeGroupName: str
    Active: bool


class CrimeHeadCreate(CrimeHeadBase):
    CrimeHeadID: int


class CrimeHeadUpdate(CrimeHeadBase):
    pass


class CrimeHeadResponse(CrimeHeadBase):
    CrimeHeadID: int

    model_config = ConfigDict(from_attributes=True)