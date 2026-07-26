from app.database.models.accused import Accused
from app.database.seeders.base_seeder import BaseSeeder


class AccusedSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        accused_list = []

        for _, row in df.iterrows():
            accused_list.append(
                Accused(
                    AccusedMasterID=row["AccusedMasterID"],
                    CaseMasterID=row["CaseMasterID"],
                    AccusedName=row["AccusedName"],
                    AgeYear=row["AgeYear"],
                    GenderID=row["GenderID"],
                    PersonID=row["PersonID"],
                )
            )

        self.db.bulk_save_objects(accused_list)
        self.db.commit()