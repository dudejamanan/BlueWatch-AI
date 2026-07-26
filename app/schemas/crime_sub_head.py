from pydantic import BaseModel, ConfigDict


class CrimeSubHeadBase(BaseModel):
    CrimeHeadID: int
    CrimeHeadName: str
    SeqID: int


class CrimeSubHeadCreate(CrimeSubHeadBase):
    CrimeSubHeadID: int


class CrimeSubHeadUpdate(CrimeSubHeadBase):
    pass


class CrimeSubHeadResponse(CrimeSubHeadBase):
    CrimeSubHeadID: int

    model_config = ConfigDict(from_attributes=True)