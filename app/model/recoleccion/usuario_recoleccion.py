from uuid import UUID
from sqlmodel import Field, SQLModel

class UsuarioRecoleccion(SQLModel, table=True):
    usuario_id: UUID = Field(foreign_key="usuario.id", primary_key=True)
    recoleccion_id: UUID = Field(foreign_key="recoleccion.id",primary_key=True)