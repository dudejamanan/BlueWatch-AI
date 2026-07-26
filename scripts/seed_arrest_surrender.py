from app.database.connection import SessionLocal
from app.database.seeders.arrest_surrender_seeder import (
    ArrestSurrenderSeeder,
)


def main():
    db = SessionLocal()

    try:
        ArrestSurrenderSeeder(db).seed(
            "datasets/raw/ArrestSurrender.csv"
        )
    finally:
        db.close()


if __name__ == "__main__":
    main()