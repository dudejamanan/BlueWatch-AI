from app.database.models.state import State
from app.database.seeders.base_seeder import BaseSeeder


class StateSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_csv(file_path)

        states = []

        for _, row in df.iterrows():
            states.append(
                State(
                    StateID=row["StateID"],
                    StateName=row["StateName"],
                    NationalityID=row["NationalityID"],
                    Active=bool(row["Active"])
                )
            )

        self.db.bulk_save_objects(states)
        self.db.commit()