from app.database.connection import SessionLocal
from app.database.seeders.state_seeder import StateSeeder


def main():
    db = SessionLocal()

    try:
        seeder = StateSeeder(db)

        seeder.seed("datasets/raw/State.csv")

        print("State table seeded successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    main()