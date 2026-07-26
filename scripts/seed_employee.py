from app.database.connection import SessionLocal
from app.database.seeders.employee_seeder import EmployeeSeeder


def main():
    db = SessionLocal()

    try:
        EmployeeSeeder(db).seed("datasets/raw/Employee.csv")
        print("Employee seeded successfully.")

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()