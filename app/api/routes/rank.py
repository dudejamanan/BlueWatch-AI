from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.rank import RankResponse
from app.services.rank_service import rank_service

router = APIRouter(
    prefix="/ranks",
    tags=["Ranks"],
)


@router.get("/", response_model=List[RankResponse])
def get_ranks(db: Session = Depends(get_db)):
    return rank_service.get_all(db)