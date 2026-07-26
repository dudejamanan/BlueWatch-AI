from pathlib import Path

import pandas as pd
from sqlalchemy.orm import Session


class BaseSeeder:
    def __init__(self, db: Session):
        self.db = db

    def read_csv(self, file_path: str):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found")

        return pd.read_csv(path)