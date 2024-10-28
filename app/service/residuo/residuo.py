from app.model.residuo.residuo import Residuo
from app.service.utils.base_service import BaseService

class ResiduoService(BaseService):
    def __init__(self, db):
        super().__init__(db, Residuo)