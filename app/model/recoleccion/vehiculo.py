from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, Optional
from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.recoleccion.recoleccion import Recoleccion

class VehiculoBase(SQLModel):
    nombre: str

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoUpdate(VehiculoBase):
    nombre: Optional[str] = None

class Vehiculo(TableBase, VehiculoBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    recolecciones: list["Recoleccion"] = Relationship(back_populates="vehiculo")