from app.database.models.gravity_offence import GravityOffence
from app.database.seeders.base_seeder import BaseSeeder


class GravityOffenceSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        gravity_offences = []

        for _, row in df.iterrows():
            gravity_offences.append(
                GravityOffence(
                    GravityOffenceID=row["GravityOffenceID"],
                    LookupValue=row["LookupValue"],
                )
            )

        self.db.bulk_save_objects(gravity_offences)
        self.db.commit()