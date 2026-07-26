from app.database.models.case_category import CaseCategory
from app.database.seeders.base_seeder import BaseSeeder


class CaseCategorySeeder(BaseSeeder):

    def seed(self, file_path: str):
        df = self.read_data(file_path)      # or read_csv() if that's your BaseSeeder

        case_categories = []

        for _, row in df.iterrows():
            case_categories.append(
                CaseCategory(
                    CaseCategoryID=row["CaseCategoryID"],
                    LookupValue=row["LookupValue"],
                )
            )

        self.db.bulk_save_objects(case_categories)
        self.db.commit()