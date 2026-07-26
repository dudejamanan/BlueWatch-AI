from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.religion_master import (
    ReligionCreate,
    ReligionResponse,
    ReligionUpdate,
)
from app.services.religion_master_service import religion_service

router = APIRouter(prefix="/religions", tags=["Religions"])


@router.post("/", response_model=ReligionResponse)
def create(data: ReligionCreate, db: Session = Depends(get_db)):
    return religion_service.create(db, data)


@router.get("/", response_model=list[ReligionResponse])
def get_all(db: Session = Depends(get_db)):
    return religion_service.get_all(db)


@router.get("/{id}", response_model=ReligionResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return religion_service.get_by_id(db, id)


@router.put("/{id}", response_model=ReligionResponse)
def update(id: int, data: ReligionUpdate, db: Session = Depends(get_db)):
    return religion_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return religion_service.delete(db, id)