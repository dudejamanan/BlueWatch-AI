from app.database.connection import SessionLocal
from app.database.seeders.unit_type_seeder import UnitTypeSeeder


def main():
    db = SessionLocal()

    try:
        UnitTypeSeeder(db).seed("datasets/raw/UnitType.csv")
        print("UnitType seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()