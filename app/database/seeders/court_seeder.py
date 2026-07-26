from app.database.models.court import Court
from app.database.seeders.base_seeder import BaseSeeder


class CourtSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        courts = []

        for _, row in df.iterrows():
            courts.append(
                Court(
                    CourtID=row["CourtID"],
                    CourtName=row["CourtName"],
                    DistrictID=row["DistrictID"],
                    StateID=row["StateID"],
                    Active=bool(row["Active"]),
                )
            )

        self.db.bulk_save_objects(courts)
        self.db.commit()