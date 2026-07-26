from app.database.connection import SessionLocal
from app.database.seeders.victim_seeder import VictimSeeder


def main():
    db = SessionLocal()
    try:
        VictimSeeder(db).seed("datasets/raw/Victim.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()