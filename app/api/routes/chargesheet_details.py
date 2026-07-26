from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.chargesheet_details import ChargesheetDetailsSchema
from app.services.chargesheet_details_service import (
    chargesheet_details_service,
)

router = APIRouter(
    prefix="/chargesheet-details",
    tags=["Chargesheet Details"],
)


@router.get("/", response_model=list[ChargesheetDetailsSchema])
def get_all(db: Session = Depends(get_db)):
    return chargesheet_details_service.get_all(db)


@router.get("/{cs_id}", response_model=ChargesheetDetailsSchema)
def get_by_id(cs_id: int, db: Session = Depends(get_db)):
    return chargesheet_details_service.get_by_id(db, cs_id)