from datetime import datetime

import pandas as pd

from app.database.models.employee import Employee
from app.database.seeders.base_seeder import BaseSeeder


class EmployeeSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        employees = []

        for row in df.itertuples(index=False):

            dob = pd.to_datetime(
                row.EmployeeDOB,
                dayfirst=True
            ).date()

            appointment = pd.to_datetime(
                row.AppointmentDate,
                dayfirst=True
            ).date()

            employees.append(
                Employee(
                    EmployeeID=row.EmployeeID,
                    DistrictID=row.DistrictID,
                    UnitID=row.UnitID,
                    RankID=row.RankID,
                    DesignationID=row.DesignationID,
                    KGID=row.KGID,
                    FirstName=row.FirstName,
                    EmployeeDOB=dob,
                    GenderID=row.GenderID,
                    BloodGroupID=row.BloodGroupID,
                    PhysicallyChallenged=bool(row.PhysicallyChallenged),
                    AppointmentDate=appointment,
                )
            )

        self.db.bulk_save_objects(employees)
        self.db.commit()