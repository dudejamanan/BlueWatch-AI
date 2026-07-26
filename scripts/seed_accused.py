from app.database.connection import SessionLocal
from app.database.seeders.accused_seeder import AccusedSeeder


def main():
    db = SessionLocal()

    try:
        AccusedSeeder(db).seed("datasets/raw/Accused.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()