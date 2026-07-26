from app.repositories.employee_repository import employee_repository
from app.services.base_service import BaseService


class EmployeeService(BaseService):
    def __init__(self):
        super().__init__(employee_repository)


employee_service = EmployeeService()