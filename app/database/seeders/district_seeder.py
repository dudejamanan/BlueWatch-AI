from app.database.models.district import District
from app.database.seeders.base_seeder import BaseSeeder


class DistrictSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        districts = [
            District(
                DistrictID=row.DistrictID,
                DistrictName=row.DistrictName,
                StateID=row.StateID,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(districts)
        self.db.commit()