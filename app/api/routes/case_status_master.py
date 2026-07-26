from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.case_status_master import (
    CaseStatusCreate,
    CaseStatusResponse,
    CaseStatusUpdate,
)
from app.services.case_status_master_service import case_status_service

router = APIRouter(prefix="/case-statuses", tags=["Case Statuses"])


@router.post("/", response_model=CaseStatusResponse)
def create(data: CaseStatusCreate, db: Session = Depends(get_db)):
    return case_status_service.create(db, data)


@router.get("/", response_model=list[CaseStatusResponse])
def get_all(db: Session = Depends(get_db)):
    return case_status_service.get_all(db)


@router.get("/{id}", response_model=CaseStatusResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return case_status_service.get_by_id(db, id)


@router.put("/{id}", response_model=CaseStatusResponse)
def update(id: int, data: CaseStatusUpdate, db: Session = Depends(get_db)):
    return case_status_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return case_status_service.delete(db, id)