from app.database.models.rank import Rank
from app.database.seeders.base_seeder import BaseSeeder


class RankSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        ranks = [
            Rank(
                RankID=row.RankID,
                RankName=row.RankName,
                Hierarchy=row.Hierarchy,
                Active=bool(row.Active),
            )
            for row in df.itertuples(index=False)
        ]

        self.db.bulk_save_objects(ranks)
        self.db.commit()