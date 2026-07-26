from app.database.models.victim import Victim
from app.database.seeders.base_seeder import BaseSeeder


class VictimSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        victims = []

        for _, row in df.iterrows():
            victims.append(
                Victim(
                    VictimMasterID=row["VictimMasterID"],
                    CaseMasterID=row["CaseMasterID"],
                    VictimName=row["VictimName"],
                    AgeYear=row["AgeYear"],
                    GenderID=row["GenderID"],
                    VictimPolice=int(row["VictimPolice"]) == 1,
                )
            )

        self.db.bulk_save_objects(victims)
        self.db.commit()