import pandas as pd

from app.database.models.arrest_surrender import ArrestSurrender
from app.database.seeders.base_seeder import BaseSeeder


class ArrestSurrenderSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        records = []

        for _, row in df.iterrows():
            records.append(
                ArrestSurrender(
                    ArrestSurrenderID=row["ArrestSurrenderID"],
                    CaseMasterID=row["CaseMasterID"],
                    ArrestSurrenderTypeID=row["ArrestSurrenderTypeID"],
                    ArrestSurrenderDate=pd.to_datetime(
                        row["ArrestSurrenderDate"],
                        dayfirst=True,
                    ).date(),
                    ArrestSurrenderStateId=row["ArrestSurrenderStateId"],
                    ArrestSurrenderDistrictId=row["ArrestSurrenderDistrictId"],
                    PoliceStationID=row["PoliceStationID"],
                    IOID=row["IOID"],
                    CourtID=row["CourtID"],
                    AccusedMasterID=row["AccusedMasterID"],
                    IsAccused=int(row["IsAccused"]) == 1,
                    IsComplainantAccused=int(row["IsComplainantAccused"]) == 1,
                )
            )

        self.db.bulk_save_objects(records)
        self.db.commit()