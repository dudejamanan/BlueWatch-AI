from app.database.models.crime_head import CrimeHead
from app.database.seeders.base_seeder import BaseSeeder


class CrimeHeadSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        objects = [
            CrimeHead(
                CrimeHeadID=row.CrimeHeadID,
                CrimeGroupName=row.CrimeGroupName,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(objects)
        self.db.commit()