from pydantic import BaseModel, ConfigDict


class CrimeHeadActSectionBase(BaseModel):
    CrimeHeadID: int
    ActCode: str
    SectionCode: str


class CrimeHeadActSectionCreate(CrimeHeadActSectionBase):
    pass


class CrimeHeadActSectionUpdate(CrimeHeadActSectionBase):
    pass


class CrimeHeadActSectionResponse(CrimeHeadActSectionBase):
    model_config = ConfigDict(from_attributes=True)