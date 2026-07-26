from app.database.models.case_status_master import CaseStatus
from app.database.seeders.base_seeder import BaseSeeder


class CaseStatusSeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)

        case_statuses = []

        for _, row in df.iterrows():
            case_statuses.append(
                CaseStatus(
                    CaseStatusID=row["CaseStatusID"],
                    CaseStatusName=row["CaseStatusName"],
                )
            )

        self.db.bulk_save_objects(case_statuses)
        self.db.commit()