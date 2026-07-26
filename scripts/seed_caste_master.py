from app.database.connection import SessionLocal
from app.database.seeders.caste_master_seeder import CasteSeeder


def main():
    db = SessionLocal()

    try:
        CasteSeeder(db).seed("datasets/raw/CasteMaster.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()