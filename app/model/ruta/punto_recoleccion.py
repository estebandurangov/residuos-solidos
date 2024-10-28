from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID
from app.model.table_base import TableBase
from app.model.ruta.punto_recoleccion_ruta import PuntoRecoleccionRuta

if TYPE_CHECKING:
    from app.model.ruta.ruta import Ruta
from app.model.ruta.promedio_residuos import PromedioResiduos

class PuntoRecoleccionBase(SQLModel):
    direccion: str
    detalles: str
    promedio_residuos: float

class PuntoRecoleccionCreate(PuntoRecoleccionBase):
    pass

class PuntoRecoleccionUpdate(PuntoRecoleccionBase):
    direccion: str | None = None
    detalles: str | None = None
    promedio_residuos: float | None = None

class PuntoRecoleccion(TableBase, PuntoRecoleccionBase, table=True):
    id: UUID = Field(default=None, primary_key=True)
    rutas: list['Ruta'] = Relationship(back_populates="puntos_recoleccion", link_model=PuntoRecoleccionRuta)
    promedios_residuos: list[PromedioResiduos] = Relationship(back_populates="punto_recoleccion")

    