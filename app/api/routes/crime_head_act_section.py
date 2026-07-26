from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.crime_head_act_section import (
    CrimeHeadActSectionResponse,
)
from app.services.crime_head_act_section_service import (
    crime_head_act_section_service,
)

router = APIRouter(
    prefix="/crime-head-act-sections",
    tags=["Crime Head Act Sections"],
)


@router.get("/", response_model=List[CrimeHeadActSectionResponse])
def get_crime_head_act_sections(db: Session = Depends(get_db)):
    return crime_head_act_section_service.get_all(db)