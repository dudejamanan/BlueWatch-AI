from app.database.connection import SessionLocal
from app.database.seeders.crime_head_act_section_seeder import (
    CrimeHeadActSectionSeeder,
)


def main():
    db = SessionLocal()

    try:
        CrimeHeadActSectionSeeder(db).seed(
            "datasets/raw/CrimeHeadActSection.csv"
        )
        print("Crime Head Act Section seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()