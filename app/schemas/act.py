from pydantic import BaseModel, ConfigDict


class ActBase(BaseModel):
    ActDescription: str
    ShortName: str
    Active: bool


class ActCreate(ActBase):
    ActCode: str


class ActUpdate(ActBase):
    pass


class ActResponse(ActBase):
    ActCode: str

    model_config = ConfigDict(from_attributes=True)