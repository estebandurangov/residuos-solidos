from app.model.ruta.tipo_ruta import TipoRuta
from app.service.utils.base_service import BaseService

class TipoRutaService(BaseService):
    def __init__(self, db):
        super().__init__(db, TipoRuta)