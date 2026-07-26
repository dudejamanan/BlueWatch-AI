from sqlalchemy.orm import Session
class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.get_all(db, skip, limit)