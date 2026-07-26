from pydantic import BaseModel, ConfigDict


class CasteBase(BaseModel):
    caste_master_name: str


class CasteCreate(CasteBase):
    caste_master_id: int


class CasteUpdate(CasteBase):
    pass


class CasteResponse(CasteBase):
    caste_master_id: int

    model_config = ConfigDict(from_attributes=True)