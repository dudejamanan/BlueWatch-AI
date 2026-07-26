from app.database.models.unit_type import UnitType
from app.database.seeders.base_seeder import BaseSeeder


class UnitTypeSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        data = [
            UnitType(
                UnitTypeID=row.UnitTypeID,
                UnitTypeName=row.UnitTypeName,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(data)
        self.db.commit()