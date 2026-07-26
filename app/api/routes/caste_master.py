from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.caste_master import (
    CasteCreate,
    CasteResponse,
    CasteUpdate,
)
from app.services.caste_master_service import caste_service

router = APIRouter(prefix="/castes", tags=["Castes"])


@router.post("/", response_model=CasteResponse)
def create(data: CasteCreate, db: Session = Depends(get_db)):
    return caste_service.create(db, data)


@router.get("/", response_model=list[CasteResponse])
def get_all(db: Session = Depends(get_db)):
    return caste_service.get_all(db)


@router.get("/{id}", response_model=CasteResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return caste_service.get_by_id(db, id)


@router.put("/{id}", response_model=CasteResponse)
def update(id: int, data: CasteUpdate, db: Session = Depends(get_db)):
    return caste_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return caste_service.delete(db, id)