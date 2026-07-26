from app.database.connection import SessionLocal
from app.database.seeders.unit_seeder import UnitSeeder


def main():
    db = SessionLocal()

    try:
        UnitSeeder(db).seed("datasets/raw/Unit.csv")
        print("Unit seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()