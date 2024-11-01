from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, List, Optional
from app.model.table_base import TableBase
from app.model.ruta.punto_recoleccion_ruta import PuntoRecoleccionRuta
from app.model.ruta.punto_recoleccion import PuntoRecoleccion
from app.model.ruta.tipo_ruta import TipoRuta

if TYPE_CHECKING:
    from app.model.recoleccion.recoleccion import Recoleccion
    from app.model.barrido.barrido import Barrido
    
class RutaBase(SQLModel):
    nombre: str
    distancia: float
    detalles: str
    tipo_ruta_id: UUID | None = Field(default=None, foreign_key="tiporuta.id") 

class RutaCreate(RutaBase):
    pass

class RutaUpdate(RutaBase):
    nombre: str | None = None
    distancia: float | None = None
    detalles: str | None = None
    tipo_ruta_id: UUID | None = None

class Ruta(TableBase, RutaBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    recolecciones: list["Recoleccion"] = Relationship(back_populates="ruta")
    barridos: list["Barrido"] = Relationship(back_populates="ruta")
    puntos_recoleccion: list[PuntoRecoleccion] = Relationship(back_populates="rutas", link_model=PuntoRecoleccionRuta)
    tipo_ruta: Optional[TipoRuta] = Relationship(back_populates="rutas")

class RutaRead(SQLModel):
    nombre: str