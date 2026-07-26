from app.database.connection import SessionLocal
from app.database.seeders.court_seeder import CourtSeeder


def main():
    db = SessionLocal()

    try:
        CourtSeeder(db).seed("datasets/raw/Court.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()