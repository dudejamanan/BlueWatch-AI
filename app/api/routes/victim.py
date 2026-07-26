from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.victim import (
    VictimCreate,
    VictimResponse,
    VictimUpdate,
)
from app.services.victim_service import victim_service

router = APIRouter(
    prefix="/victims",
    tags=["Victims"],
)


@router.post("/", response_model=VictimResponse)
def create(data: VictimCreate, db: Session = Depends(get_db)):
    return victim_service.create(db, data)


@router.get("/", response_model=list[VictimResponse])
def get_all(db: Session = Depends(get_db)):
    return victim_service.get_all(db)


@router.get("/{id}", response_model=VictimResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return victim_service.get_by_id(db, id)


@router.put("/{id}", response_model=VictimResponse)
def update(id: int, data: VictimUpdate, db: Session = Depends(get_db)):
    return victim_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return victim_service.delete(db, id)