from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.crime_head import CrimeHeadResponse
from app.services.crime_head_service import crime_head_service

router = APIRouter(
    prefix="/crime-heads",
    tags=["Crime Heads"],
)


@router.get("/", response_model=List[CrimeHeadResponse])
def get_crime_heads(db: Session = Depends(get_db)):
    return crime_head_service.get_all(db)