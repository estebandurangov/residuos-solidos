from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, Optional
from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.recoleccion.recoleccion import Recoleccion


class VehiculoBase(SQLModel):
    placa: str = Field(primary_key=True)
    kilometraje: int
    capacidad: float


class VehiculoCreate(VehiculoBase):
    pass


class VehiculoUpdate(VehiculoBase):
    placa: str | None = None
    kilometraje: int | None = None
    capacidad: float | None = None


class Vehiculo(TableBase, VehiculoBase, table=True):
    recolecciones: list["Recoleccion"] = Relationship(back_populates="vehiculo")


class VehiculoRead(SQLModel):
    placa: str


