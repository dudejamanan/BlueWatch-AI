from app.database.connection import SessionLocal
from app.database.seeders.crime_head_seeder import CrimeHeadSeeder


def main():
    db = SessionLocal()

    try:
        CrimeHeadSeeder(db).seed("datasets/raw/CrimeHead.csv")
        print("Crime Head seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()