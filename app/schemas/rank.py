from pydantic import BaseModel, ConfigDict


class RankResponse(BaseModel):
    RankID: int
    RankName: str
    Hierarchy: int
    Active: bool

    model_config = ConfigDict(from_attributes=True)