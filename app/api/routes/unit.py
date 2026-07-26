from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.unit import UnitResponse
from app.services.unit_service import unit_service

router = APIRouter(
    prefix="/units",
    tags=["Units"],
)


@router.get("/", response_model=List[UnitResponse])
def get_units(
    district_id: int | None = None,
    db: Session = Depends(get_db),
):
    if district_id is None:
        return unit_service.get_all(db)

    return unit_service.get_by_district(db, district_id)