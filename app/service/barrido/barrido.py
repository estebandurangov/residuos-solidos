from app.model.barrido.barrido import Barrido
from app.service.utils.base_service import BaseService

class BarridoService(BaseService):
    def __init__(self, db):
        super().__init__(db, Barrido)