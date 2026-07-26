from app.database.models.complainant_details import Complainant
from app.database.seeders.base_seeder import BaseSeeder


class ComplainantSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        complainants = []

        for _, row in df.iterrows():
            complainants.append(
                Complainant(
                    ComplainantID=row["ComplainantID"],
                    CaseMasterID=row["CaseMasterID"],
                    ComplainantName=row["ComplainantName"],
                    AgeYear=row["AgeYear"],
                    OccupationID=row["OccupationID"],
                    ReligionID=row["ReligionID"],
                    CasteID=row["CasteID"],
                    GenderID=row["GenderID"],
                )
            )

        self.db.bulk_save_objects(complainants)
        self.db.commit()