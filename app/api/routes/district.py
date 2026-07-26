from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.district import DistrictResponse
from app.services.district_service import district_service

router = APIRouter(
    prefix="/districts",
    tags=["Districts"],
)


@router.get("/", response_model=List[DistrictResponse])
def get_districts(
    state_id: int | None = None,
    db: Session = Depends(get_db),
):
    if state_id is None:
        return district_service.get_all(db)

    return district_service.get_by_state(db, state_id)