from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.designation import DesignationResponse
from app.services.designation_service import designation_service

router = APIRouter(
    prefix="/designations",
    tags=["Designations"],
)


@router.get("/", response_model=List[DesignationResponse])
def get_designations(db: Session = Depends(get_db)):
    return designation_service.get_all(db)