from app.database.connection import SessionLocal
from app.database.seeders.rank_seeder import RankSeeder


def main():
    db = SessionLocal()

    try:
        RankSeeder(db).seed("datasets/raw/Rank.csv")
        print("Rank seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()