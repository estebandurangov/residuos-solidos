from app.model.ruta.ruta import Ruta
from app.service.utils.base_service import BaseService

class RutaService(BaseService):
    def __init__(self, db):
        super().__init__(db, Ruta)