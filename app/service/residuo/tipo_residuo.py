from app.model.residuo.tipo_residuo import TipoResiduo
from app.service.utils.base_service import BaseService

class TipoResiduoService(BaseService):
    def __init__(self, db):
        super().__init__(db, TipoResiduo)