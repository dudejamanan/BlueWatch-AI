from app.database.connection import SessionLocal
from app.database.seeders.case_master_seeder import CaseMasterSeeder


def main():
    db = SessionLocal()

    try:
        CaseMasterSeeder(db).seed("datasets/raw/CaseMaster.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()