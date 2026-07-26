from app.database.models.designation import Designation
from app.database.seeders.base_seeder import BaseSeeder


class DesignationSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        designations = [
            Designation(
                DesignationID=row.DesignationID,
                DesignationName=row.DesignationName,
                SortOrder=row.SortOrder,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(designations)
        self.db.commit()