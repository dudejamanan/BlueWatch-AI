from pydantic import BaseModel, ConfigDict


class DistrictResponse(BaseModel):
    DistrictID: int
    DistrictName: str
    StateID: int
    Active: bool

    model_config = ConfigDict(from_attributes=True)