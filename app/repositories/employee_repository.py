from app.database.models.employee import Employee
from app.repositories.base_repository import BaseRepository


class EmployeeRepository(BaseRepository[Employee]):
    def __init__(self):
        super().__init__(Employee)


employee_repository = EmployeeRepository()