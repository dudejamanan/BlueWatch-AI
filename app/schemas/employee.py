from datetime import date

from pydantic import BaseModel, ConfigDict


class EmployeeResponse(BaseModel):
    EmployeeID: int
    DistrictID: int
    UnitID: int
    RankID: int
    DesignationID: int
    KGID: str
    FirstName: str
    EmployeeDOB: date
    GenderID: int
    BloodGroupID: int
    PhysicallyChallenged: bool
    AppointmentDate: date

    model_config = ConfigDict(from_attributes=True)