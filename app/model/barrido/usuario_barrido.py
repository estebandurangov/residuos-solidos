from uuid import UUID
from sqlmodel import Field, SQLModel

class UsuarioBarrido(SQLModel, table=True):
    usuario_id: UUID = Field(default=None, foreign_key="usuario.id", primary_key=True)
    barrido_id: UUID = Field(default=None, foreign_key="barrido.id", primary_key=True)