from app.database.models.unit import Unit
from app.database.seeders.base_seeder import BaseSeeder


class UnitSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        units = [
            Unit(
                UnitID=row.UnitID,
                UnitName=row.UnitName,
                TypeID=row.TypeID,
                ParentUnit=None if row.ParentUnit != row.ParentUnit else row.ParentUnit,
                NationalityID=row.NationalityID,
                StateID=row.StateID,
                DistrictID=row.DistrictID,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(units)
        self.db.commit()