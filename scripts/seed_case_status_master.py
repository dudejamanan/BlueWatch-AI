from app.database.connection import SessionLocal
from app.database.seeders.case_status_master_seeder import CaseStatusSeeder


def main():
    db = SessionLocal()

    try:
        CaseStatusSeeder(db).seed("datasets/raw/CaseStatusMaster.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()