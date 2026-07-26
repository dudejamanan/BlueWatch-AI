from app.database.models.crime_head_act_section import CrimeHeadActSection
from app.database.seeders.base_seeder import BaseSeeder


class CrimeHeadActSectionSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        objects = [
            CrimeHeadActSection(
                CrimeHeadID=row.CrimeHeadID,
                ActCode=row.ActCode,
                SectionCode=row.SectionCode,
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(objects)
        self.db.commit()