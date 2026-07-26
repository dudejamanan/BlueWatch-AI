from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.occupation_master import (
    OccupationCreate,
    OccupationResponse,
    OccupationUpdate,
)
from app.services.occupation_master_service import occupation_service

router = APIRouter(prefix="/occupations", tags=["Occupations"])


@router.post("/", response_model=OccupationResponse)
def create(data: OccupationCreate, db: Session = Depends(get_db)):
    return occupation_service.create(db, data)


@router.get("/", response_model=list[OccupationResponse])
def get_all(db: Session = Depends(get_db)):
    return occupation_service.get_all(db)


@router.get("/{id}", response_model=OccupationResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return occupation_service.get_by_id(db, id)


@router.put("/{id}", response_model=OccupationResponse)
def update(id: int, data: OccupationUpdate, db: Session = Depends(get_db)):
    return occupation_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return occupation_service.delete(db, id)