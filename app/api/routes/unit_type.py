from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.unit_type import UnitTypeResponse
from app.services.unit_type_service import unit_type_service

router = APIRouter(
    prefix="/unit-types",
    tags=["Unit Types"],
)


@router.get("/", response_model=List[UnitTypeResponse])
def get_unit_types(db: Session = Depends(get_db)):
    return unit_type_service.get_all(db)