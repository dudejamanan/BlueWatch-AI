from app.database.connection import SessionLocal
from app.database.seeders.complainant_details_seeder import ComplainantSeeder


def main():
    db = SessionLocal()

    try:
        ComplainantSeeder(db).seed("datasets/raw/ComplainantDetails.csv")
    finally:
        db.close()


if __name__ == "__main__":
    main()