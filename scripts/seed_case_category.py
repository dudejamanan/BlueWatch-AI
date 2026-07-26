from app.database.connection import SessionLocal
from app.database.seeders.case_category_seeder import CaseCategorySeeder


def main():
    db = SessionLocal()

    try:
        CaseCategorySeeder(db).seed("datasets/raw/CaseCategory.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()