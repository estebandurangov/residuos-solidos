from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID
from app.model.table_base import TableBase
from app.model.ruta.punto_recoleccion_ruta import PuntoRecoleccionRuta

if TYPE_CHECKING:
    from app.model.ruta.ruta import Ruta

class PuntoRecoleccionBase(SQLModel):
    direccion: str
    detalles: str
    

class PuntoRecoleccionCreate(PuntoRecoleccionBase):
    pass

class PuntoRecoleccionUpdate(PuntoRecoleccionBase):
    direccion: str | None = None
    detalles: str | None = None

class PuntoRecoleccion(TableBase, PuntoRecoleccionBase, table=True):
    id: UUID = Field(default=None, primary_key=True)
    rutas: list["Ruta"] = Relationship(back_populates="puntos_recoleccion", link_model=PuntoRecoleccionRuta)
    

    