from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.case_master import (
    CaseMasterCreate,
    CaseMasterResponse,
    CaseMasterUpdate,
)
from app.services.case_master_service import case_master_service

router = APIRouter(
    prefix="/case-masters",
    tags=["Case Masters"],
)


@router.post("/", response_model=CaseMasterResponse)
def create(data: CaseMasterCreate, db: Session = Depends(get_db)):
    return case_master_service.create(db, data)


@router.get("/", response_model=list[CaseMasterResponse])
def get_all(db: Session = Depends(get_db)):
    return case_master_service.get_all(db)


@router.get("/{id}", response_model=CaseMasterResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return case_master_service.get_by_id(db, id)


@router.put("/{id}", response_model=CaseMasterResponse)
def update(id: int, data: CaseMasterUpdate, db: Session = Depends(get_db)):
    return case_master_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return case_master_service.delete(db, id)