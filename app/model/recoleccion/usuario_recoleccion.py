from uuid import UUID
from sqlmodel import Field, SQLModel

class UsuarioRecoleccion(SQLModel, table=True):
    id_usuario: UUID = Field(foreign_key="usuario.id", primary_key=True)
    id_recoleccion: UUID = Field(foreign_key="recoleccion.id",primary_key=True)