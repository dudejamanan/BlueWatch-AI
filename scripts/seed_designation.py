from app.database.connection import SessionLocal
from app.database.seeders.designation_seeder import DesignationSeeder


def main():
    db = SessionLocal()

    try:
        DesignationSeeder(db).seed("datasets/raw/Designation.csv")
        print("Designation seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()