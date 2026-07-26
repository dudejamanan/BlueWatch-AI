from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.section import SectionResponse
from app.services.section_service import section_service

router = APIRouter(
    prefix="/sections",
    tags=["Sections"],
)


@router.get("/", response_model=List[SectionResponse])
def get_sections(db: Session = Depends(get_db)):
    return section_service.get_all(db)