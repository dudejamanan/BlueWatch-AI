from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.employee import EmployeeResponse
from app.services.employee_service import employee_service

from typing import List

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)




@router.get("/", response_model=List[EmployeeResponse])
def get_employees(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return employee_service.get_all(db, skip, limit)