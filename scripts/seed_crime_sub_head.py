from app.database.connection import SessionLocal
from app.database.seeders.crime_sub_head_seeder import CrimeSubHeadSeeder


def main():
    db = SessionLocal()

    try:
        CrimeSubHeadSeeder(db).seed("datasets/raw/CrimeSubHead.csv")
        print("Crime Sub Head seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()