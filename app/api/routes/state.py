from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.state_service import state_service
from typing import List
from app.schemas.state import StateResponse
router = APIRouter(
    prefix="/states",
    tags=["States"],
)


@router.get("/", response_model=List[StateResponse])
def get_states(db: Session = Depends(get_db)):
    return state_service.get_all(db)