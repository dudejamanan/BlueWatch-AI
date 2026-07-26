from app.database.connection import SessionLocal
from app.database.seeders.district_seeder import DistrictSeeder


def main():
    db = SessionLocal()

    try:
        DistrictSeeder(db).seed("datasets/raw/District.csv")
        print("District table seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()