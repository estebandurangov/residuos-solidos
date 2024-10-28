from app.model.barrido.usuario_barrido import UsuarioBarrido
from app.service.utils.base_service import BaseService

class UsuarioBarridoService(BaseService):
    def __init__(self, db):
        super().__init__(db, UsuarioBarrido)