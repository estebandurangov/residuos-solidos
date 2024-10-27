from typing import TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4

from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.ruta.ruta import Ruta

class TipoRutaBase(SQLModel):
    nombre: str
    descripcion: str


class TipoRutaCreate(TipoRutaBase):
    pass

class TipoRutaUpdate(TipoRutaBase):
    nombre: str | None = None
    descripcion: str | None = None

class TipoRuta(TableBase, TipoRutaBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    rutas: list["Ruta"] = Relationship(back_populates="tipo_ruta")