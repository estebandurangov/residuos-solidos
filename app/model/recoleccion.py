from uuid import UUID, uuid4
from app.model.table_base import TableBase
from sqlmodel import Field, SQLModel
from datetime import datetime

class RecoleccionBase(SQLModel):
    fecha_inicio: datetime
    fecha_fin: datetime
    peso: float
    observaciones: str
    detalle: str
    vehiculo_id: UUID
    ruta_id: UUID
    tipo_residuo_id: UUID


class RecoleccionCreate(RecoleccionBase):
    pass

class RecoleccionUpdate(RecoleccionBase):
    fecha_inicio: datetime | None = None
    fecha_fin: datetime | None = None
    peso: float | None = None
    observaciones: str | None = None
    detalle: str | None = None
    vehiculo_id: UUID | None = None
    ruta_id: UUID | None = None
    tipo_residuo_id: UUID | None = None

class Recoleccion(TableBase, RecoleccionBase, table=True):
    id: UUID | None = Field(primary_key=True, default_factory=uuid4)