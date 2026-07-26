from pydantic import BaseModel, ConfigDict


class CaseCategoryBase(BaseModel):
    LookupValue: str


class CaseCategoryCreate(CaseCategoryBase):
    CaseCategoryID: int


class CaseCategoryUpdate(CaseCategoryBase):
    pass


class CaseCategoryResponse(CaseCategoryBase):
    CaseCategoryID: int

    model_config = ConfigDict(from_attributes=True)