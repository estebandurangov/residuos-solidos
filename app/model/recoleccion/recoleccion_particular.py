from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.recoleccion.recoleccion import Recoleccion

class RecoleccionParticularBase(SQLModel):
    recoleccion_id: UUID = Field(foreign_key="recoleccion.id")
    metraje: float
    tipo_documento_responsable: str
    documento_responsable: str
    nombre_responsable: str
    email_responsable: str

class RecoleccionParticularCreate(RecoleccionParticularBase):
    pass

class RecoleccionParticularUpdate(RecoleccionParticularBase):
    metraje: float | None = None
    tipo_documento_responsable: str | None = None
    documento_responsable: str | None = None
    nombre_responsable: str | None = None
    email_responsable: str | None = None

class RecoleccionParticular(TableBase, RecoleccionParticularBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)

    recoleccion: 'Recoleccion' = Relationship(back_populates="recolecciones_particulares")