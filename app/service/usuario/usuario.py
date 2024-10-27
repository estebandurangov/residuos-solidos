from app.model.usuario.usuario import Usuario
from app.service.utils.base_service import BaseService

class UsuarioService(BaseService):
    def __init__(self, db):
        super().__init__(db, Usuario)