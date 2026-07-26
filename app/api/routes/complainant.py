from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.complainant import (
    ComplainantCreate,
    ComplainantResponse,
    ComplainantUpdate,
)
from app.services.complainant_service import complainant_service

router = APIRouter(
    prefix="/complainants",
    tags=["Complainants"],
)


@router.post("/", response_model=ComplainantResponse)
def create(data: ComplainantCreate, db: Session = Depends(get_db)):
    return complainant_service.create(db, data)


@router.get("/", response_model=list[ComplainantResponse])
def get_all(db: Session = Depends(get_db)):
    return complainant_service.get_all(db)


@router.get("/{id}", response_model=ComplainantResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return complainant_service.get_by_id(db, id)


@router.put("/{id}", response_model=ComplainantResponse)
def update(id: int, data: ComplainantUpdate, db: Session = Depends(get_db)):
    return complainant_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return complainant_service.delete(db, id)