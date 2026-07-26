from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.court import (
    CourtCreate,
    CourtResponse,
    CourtUpdate,
)
from app.services.court_service import court_service

router = APIRouter(
    prefix="/courts",
    tags=["Courts"],
)


@router.post("/", response_model=CourtResponse)
def create(data: CourtCreate, db: Session = Depends(get_db)):
    return court_service.create(db, data)


@router.get("/", response_model=list[CourtResponse])
def get_all(db: Session = Depends(get_db)):
    return court_service.get_all(db)


@router.get("/{id}", response_model=CourtResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return court_service.get_by_id(db, id)


@router.put("/{id}", response_model=CourtResponse)
def update(id: int, data: CourtUpdate, db: Session = Depends(get_db)):
    return court_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return court_service.delete(db, id)