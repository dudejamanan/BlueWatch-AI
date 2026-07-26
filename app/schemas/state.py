from pydantic import BaseModel, ConfigDict


class StateResponse(BaseModel):
    StateID: int
    StateName: str
    NationalityID: int
    Active: bool

    model_config = ConfigDict(from_attributes=True)