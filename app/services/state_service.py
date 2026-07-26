from app.repositories.state_repository import state_repository
from app.services.base_service import BaseService

state_service = BaseService(state_repository)