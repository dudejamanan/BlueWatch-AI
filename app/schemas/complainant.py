from pydantic import BaseModel, ConfigDict


class ComplainantBase(BaseModel):
    CaseMasterID: int
    ComplainantName: str
    AgeYear: int
    OccupationID: int
    ReligionID: int
    CasteID: int
    GenderID: int


class ComplainantCreate(ComplainantBase):
    ComplainantID: int


class ComplainantUpdate(ComplainantBase):
    pass


class ComplainantResponse(ComplainantBase):
    ComplainantID: int

    model_config = ConfigDict(from_attributes=True)