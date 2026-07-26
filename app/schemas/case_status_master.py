from pydantic import BaseModel, ConfigDict


class CaseStatusBase(BaseModel):
    CaseStatusName: str


class CaseStatusCreate(CaseStatusBase):
    CaseStatusID: int


class CaseStatusUpdate(CaseStatusBase):
    pass


class CaseStatusResponse(CaseStatusBase):
    CaseStatusID: int

    model_config = ConfigDict(from_attributes=True)