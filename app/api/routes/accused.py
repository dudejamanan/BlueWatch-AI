from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.accused import (
    AccusedCreate,
    AccusedResponse,
    AccusedUpdate,
)
from app.services.accused_service import accused_service

router = APIRouter(
    prefix="/accused",
    tags=["Accused"],
)


@router.post("/", response_model=AccusedResponse)
def create(data: AccusedCreate, db: Session = Depends(get_db)):
    return accused_service.create(db, data)


@router.get("/", response_model=list[AccusedResponse])
def get_all(db: Session = Depends(get_db)):
    return accused_service.get_all(db)


@router.get("/{id}", response_model=AccusedResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return accused_service.get_by_id(db, id)


@router.put("/{id}", response_model=AccusedResponse)
def update(id: int, data: AccusedUpdate, db: Session = Depends(get_db)):
    return accused_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return accused_service.delete(db, id)