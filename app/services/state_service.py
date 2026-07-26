from sqlalchemy.orm import Session

from app.repositories.state_repository import StateRepository


class StateService:

    @staticmethod
    def get_all_states(db: Session):
        return StateRepository.get_all(db)