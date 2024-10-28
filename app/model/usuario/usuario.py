from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship

from app.model.table_base import TableBase

from app.model.recoleccion.usuario_recoleccion import UsuarioRecoleccion
from app.model.recoleccion.recoleccion import Recoleccion
from app.model.barrido.barrido import Barrido
from app.model.barrido.usuario_barrido import UsuarioBarrido

from app.model.usuario.rol import Rol

if TYPE_CHECKING:
    from app.model.usuario.users import Users


class UsuarioBase(SQLModel):
    id: UUID = Field(primary_key=True, foreign_key="auth.users.id")
    nombre: str
    tipo_documento: str
    documento: str
    rol_id: UUID = Field(foreign_key="rol.id")

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    nombre: str | None = None
    tipo_documento: str | None = None
    documento: str | None = None
    rol_id: UUID | None = None

class Usuario(TableBase, UsuarioBase, table=True):
    
    rol: Rol = Relationship(back_populates="usuarios")

    recolecciones: Recoleccion = Relationship(back_populates="usuarios", link_model=UsuarioRecoleccion)
    barridos: Barrido = Relationship(back_populates="usuarios", link_model=UsuarioBarrido)
    user: "Users" = Relationship(back_populates="usuario")