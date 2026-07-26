from app.database.connection import SessionLocal
from app.database.seeders.occupation_master_seeder import OccupationSeeder


def main():
    db = SessionLocal()

    try:
        OccupationSeeder(db).seed("datasets/raw/OccupationMaster.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()