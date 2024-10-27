from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship

from app.model.table_base import TableBase

from app.model.recoleccion.recoleccion import Recoleccion
from app.model.recoleccion.usuario_recoleccion import UsuarioRecoleccion
from app.model.barrido.barrido import Barrido
from app.model.barrido.usuario_barrido import UsuarioBarrido

from app.model.usuario.rol import Rol
from app.model.usuario.users import Users

class UsuarioBase(SQLModel):
    # id: UUID = Field(foreign_key="auth.users.id", primary_key=True)
    rol_id: UUID = Field(foreign_key="rol.id")

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    rol_id: UUID | None = None

class Usuario(TableBase, UsuarioBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    rol: Rol = Relationship(back_populates="usuarios")

    recolecciones: Recoleccion = Relationship(back_populates="usuario", link_model=UsuarioRecoleccion)
    barridos: Barrido = Relationship(back_populates="usuario", link_model=UsuarioBarrido)
    user: Users = Relationship(back_populates="usuario")