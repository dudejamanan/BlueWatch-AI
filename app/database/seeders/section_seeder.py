from app.database.models.section import Section
from app.database.seeders.base_seeder import BaseSeeder


class SectionSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        objects = [
            Section(
                ActCode=row.ActCode,
                SectionCode=row.SectionCode,
                SectionDescription=row.SectionDescription,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(objects)
        self.db.commit()