from app.database.connection import SessionLocal
from app.database.seeders.gravity_offence_seeder import GravityOffenceSeeder


def main():
    db = SessionLocal()

    try:
        GravityOffenceSeeder(db).seed("datasets/raw/GravityOffence.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()