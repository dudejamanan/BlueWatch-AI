class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self, db):
        return self.repository.get_all(db)