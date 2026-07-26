from pydantic import BaseModel, ConfigDict


class UnitResponse(BaseModel):
    UnitID: int
    UnitName: str
    TypeID: int
    ParentUnit: int | None
    NationalityID: int
    StateID: int
    DistrictID: int
    Active: bool

    model_config = ConfigDict(from_attributes=True)