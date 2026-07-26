from pydantic import BaseModel, ConfigDict


class DesignationResponse(BaseModel):
    DesignationID: int
    DesignationName: str
    SortOrder: int
    Active: bool

    model_config = ConfigDict(from_attributes=True)