from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.state_service import StateService

router = APIRouter(
    prefix="/states",
    tags=["States"]
)


@router.get("/")
def get_states(db: Session = Depends(get_db)):
    return StateService.get_all_states(db)