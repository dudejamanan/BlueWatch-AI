from app.database.models.act import Act
from app.database.seeders.base_seeder import BaseSeeder


class ActSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        objects = [
            Act(
                ActCode=row.ActCode,
                ActDescription=row.ActDescription,
                ShortName=row.ShortName,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(objects)
        self.db.commit()