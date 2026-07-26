from pydantic import BaseModel, ConfigDict


class UnitTypeResponse(BaseModel):
    UnitTypeID: int
    UnitTypeName: str
    Active: bool

    model_config = ConfigDict(from_attributes=True)