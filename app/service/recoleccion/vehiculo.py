from app.model.recoleccion.vehiculo import Vehiculo
from app.service.utils.base_service import BaseService

class VehiculoService(BaseService):
    def __init__(self, db):
        super().__init__(db, Vehiculo)
