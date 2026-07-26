from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.gravity_offence import (
    GravityOffenceCreate,
    GravityOffenceResponse,
    GravityOffenceUpdate,
)
from app.services.gravity_offence_service import gravity_offence_service

router = APIRouter(prefix="/gravity-offences", tags=["Gravity Offences"])


@router.post("/", response_model=GravityOffenceResponse)
def create(data: GravityOffenceCreate, db: Session = Depends(get_db)):
    return gravity_offence_service.create(db, data)


@router.get("/", response_model=list[GravityOffenceResponse])
def get_all(db: Session = Depends(get_db)):
    return gravity_offence_service.get_all(db)


@router.get("/{id}", response_model=GravityOffenceResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return gravity_offence_service.get_by_id(db, id)


@router.put("/{id}", response_model=GravityOffenceResponse)
def update(id: int, data: GravityOffenceUpdate, db: Session = Depends(get_db)):
    return gravity_offence_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return gravity_offence_service.delete(db, id)