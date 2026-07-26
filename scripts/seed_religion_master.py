from app.database.connection import SessionLocal
from app.database.seeders.religion_master_seeder import ReligionSeeder


def main():
    db = SessionLocal()

    try:
        ReligionSeeder(db).seed("datasets/raw/ReligionMaster.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()