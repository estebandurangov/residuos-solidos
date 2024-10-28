from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.ruta.punto_recoleccion import PuntoRecoleccion

class PromedioResiduos(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    punto_recoleccion_id: UUID = Field(foreign_key="puntorecoleccion.id")
    tipo_residuo_id: UUID = Field(foreign_key="tiporesiduo.id")
    promedio: float

    punto_recoleccion: 'PuntoRecoleccion' = Relationship(back_populates="promedios_residuos")