from pydantic import BaseModel, ConfigDict


class SectionBase(BaseModel):
    SectionDescription: str
    Active: bool


class SectionCreate(SectionBase):
    ActCode: str
    SectionCode: str


class SectionUpdate(SectionBase):
    pass


class SectionResponse(SectionBase):
    ActCode: str
    SectionCode: str

    model_config = ConfigDict(from_attributes=True)