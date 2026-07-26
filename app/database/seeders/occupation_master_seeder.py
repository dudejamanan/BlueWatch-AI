from app.database.models.occupation_master import Occupation
from app.database.seeders.base_seeder import BaseSeeder


class OccupationSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        occupations = []

        for _, row in df.iterrows():
            occupations.append(
                Occupation(
                    OccupationID=row["OccupationID"],
                    OccupationName=row["OccupationName"],
                )
            )

        self.db.bulk_save_objects(occupations)
        self.db.commit()