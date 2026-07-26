from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.crime_sub_head import CrimeSubHeadResponse
from app.services.crime_sub_head_service import crime_sub_head_service

router = APIRouter(
    prefix="/crime-sub-heads",
    tags=["Crime Sub Heads"],
)


@router.get("/", response_model=List[CrimeSubHeadResponse])
def get_crime_sub_heads(db: Session = Depends(get_db)):
    return crime_sub_head_service.get_all(db)