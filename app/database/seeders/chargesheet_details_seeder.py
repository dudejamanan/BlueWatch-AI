import pandas as pd

from app.database.models.chargesheet_details import ChargesheetDetails
from app.database.seeders.base_seeder import BaseSeeder


class ChargesheetDetailsSeeder(BaseSeeder):
    def seed(self, file_path: str):
        df = self.read_data(file_path)

        records = []

        for _, row in df.iterrows():
            records.append(
                ChargesheetDetails(
                    CSID=int(row["CSID"]),
                    CaseMasterID=int(row["CaseMasterID"]),
                    csdate=pd.to_datetime(
                        row["csdate"],
                        dayfirst=True,
                    ).date(),
                    cstype=row["cstype"],
                    PolicePersonID=int(row["PolicePersonID"]),
                )
            )

        self.db.bulk_save_objects(records)
        self.db.commit()