from app.model.usuario.users import Users
from app.service.utils.base_service import BaseService

class UserService(BaseService):
    def __init__(self, db):
        super().__init__(db, Users)
