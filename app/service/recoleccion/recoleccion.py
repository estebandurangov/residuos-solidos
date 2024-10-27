from app.model.recoleccion.recoleccion import Recoleccion
from app.service.utils.base_service import BaseService

class RecoleccionService(BaseService):
    def __init__(self, db):
        super().__init__(db, Recoleccion)

