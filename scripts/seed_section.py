from app.database.connection import SessionLocal
from app.database.seeders.section_seeder import SectionSeeder


def main():
    db = SessionLocal()

    try:
        SectionSeeder(db).seed("datasets/raw/Section.csv")
        print("Section seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()