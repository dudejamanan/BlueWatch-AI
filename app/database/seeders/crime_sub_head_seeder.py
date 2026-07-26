from app.database.models.crime_sub_head import CrimeSubHead
from app.database.seeders.base_seeder import BaseSeeder


class CrimeSubHeadSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        objects = [
            CrimeSubHead(
                CrimeSubHeadID=row.CrimeSubHeadID,
                CrimeHeadID=row.CrimeHeadID,
                CrimeHeadName=row.CrimeHeadName,
                SeqID=row.SeqID,
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(objects)
        self.db.commit()