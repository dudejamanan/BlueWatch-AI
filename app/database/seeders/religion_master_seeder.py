from app.database.models.religion_master import Religion
from app.database.seeders.base_seeder import BaseSeeder


class ReligionSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        religions = []

        for _, row in df.iterrows():
            religions.append(
                Religion(
                    ReligionID=row["ReligionID"],
                    ReligionName=row["ReligionName"],
                )
            )

        self.db.bulk_save_objects(religions)
        self.db.commit()