from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.act import ActResponse
from app.services.act_service import act_service

router = APIRouter(
    prefix="/acts",
    tags=["Acts"],
)


@router.get("/", response_model=List[ActResponse])
def get_acts(db: Session = Depends(get_db)):
    return act_service.get_all(db)