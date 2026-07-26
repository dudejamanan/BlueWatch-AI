import pandas as pd

from app.database.models.case_master import CaseMaster
from app.database.seeders.base_seeder import BaseSeeder


class CaseMasterSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        cases = []

        for _, row in df.iterrows():
            cases.append(
                CaseMaster(
                    CaseMasterID=row["CaseMasterID"],
                    CrimeNo=str(row["CrimeNo"]),
                    CaseNo=str(row["CaseNo"]),
                    CrimeRegisteredDate=pd.to_datetime(
                        row["CrimeRegisteredDate"],
                        dayfirst=True,
                    ).date(),
                    PolicePersonID=row["PolicePersonID"],
                    PoliceStationID=row["PoliceStationID"],
                    CaseCategoryID=row["CaseCategoryID"],
                    GravityOffenceID=row["GravityOffenceID"],
                    CrimeMajorHeadID=row["CrimeMajorHeadID"],
                    CrimeMinorHeadID=row["CrimeMinorHeadID"],
                    CaseStatusID=row["CaseStatusID"],
                    CourtID=(
                        None
                        if pd.isna(row["CourtID"]) or row["CourtID"] == ""
                        else int(row["CourtID"])
                    ),
                    IncidentFromDate=pd.to_datetime(
                        row["IncidentFromDate"],
                        dayfirst=True,
                    ),
                    IncidentToDate=pd.to_datetime(
                        row["IncidentToDate"],
                        dayfirst=True,
                    ),
                    InfoReceivedPSDate=pd.to_datetime(
                        row["InfoReceivedPSDate"],
                        dayfirst=True,
                    ),
                    latitude=float(row["latitude"]),
                    longitude=float(row["longitude"]),
                    BriefFacts=row["BriefFacts"],
                )
            )

        self.db.bulk_save_objects(cases)
        self.db.commit()