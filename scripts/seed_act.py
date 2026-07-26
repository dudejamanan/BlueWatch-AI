from app.database.connection import SessionLocal
from app.database.seeders.act_seeder import ActSeeder


def main():
    db = SessionLocal()

    try:
        ActSeeder(db).seed("datasets/raw/Act.csv")
        print("Act seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()