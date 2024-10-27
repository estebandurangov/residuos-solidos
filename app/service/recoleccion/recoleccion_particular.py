from app.model.recoleccion.recoleccion_particular import RecoleccionParticular
from app.service.utils.base_service import BaseService

class RecoleccionParticularService(BaseService):
    def __init__(self, db):
        super().__init__(db, RecoleccionParticular)