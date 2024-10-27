from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.usuario.usuario import Usuario

class RolBase(SQLModel):
    nombre: str
    descripcion: str

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    nombre: str | None = None
    descripcion: str | None = None

class Rol(TableBase, RolBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    usuarios: list["Usuario"] = Relationship(back_populates="rol")