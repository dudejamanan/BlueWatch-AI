from app.database.models.caste_master import Caste
from app.database.seeders.base_seeder import BaseSeeder


class CasteSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        castes = []

        for _, row in df.iterrows():
            castes.append(
                Caste(
                    caste_master_id=row["caste_master_id"],
                    caste_master_name=row["caste_master_name"],
                )
            )

        self.db.bulk_save_objects(castes)
        self.db.commit()