from app.database.connection import SessionLocal
from app.database.seeders.chargesheet_details_seeder import (
    ChargesheetDetailsSeeder,
)


def main():
    db = SessionLocal()
    try:
        ChargesheetDetailsSeeder(db).seed(
            "datasets/raw/ChargesheetDetails.csv"
        )
    finally:
        db.close()


if __name__ == "__main__":
    main()