from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.case_category import (
    CaseCategoryCreate,
    CaseCategoryResponse,
    CaseCategoryUpdate,
)
from app.services.case_category_service import case_category_service

router = APIRouter(prefix="/case-categories", tags=["Case Categories"])


@router.post("/", response_model=CaseCategoryResponse)
def create(data: CaseCategoryCreate, db: Session = Depends(get_db)):
    return case_category_service.create(db, data)


@router.get("/", response_model=list[CaseCategoryResponse])
def get_all(db: Session = Depends(get_db)):
    return case_category_service.get_all(db)


@router.get("/{id}", response_model=CaseCategoryResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return case_category_service.get_by_id(db, id)


@router.put("/{id}", response_model=CaseCategoryResponse)
def update(id: int, data: CaseCategoryUpdate, db: Session = Depends(get_db)):
    return case_category_service.update(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return case_category_service.delete(db, id)