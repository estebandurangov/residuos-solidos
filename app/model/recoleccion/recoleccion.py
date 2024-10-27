from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from app.model.table_base import TableBase
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

from app.model.recoleccion.usuario_recoleccion import UsuarioRecoleccion
from app.model.recoleccion.vehiculo import Vehiculo
from app.model.ruta.ruta import Ruta
# 

if TYPE_CHECKING:
    from app.model.usuario.usuario import Usuario
from app.model.residuo.tipo_residuo import TipoResiduo
from app.model.recoleccion.recoleccion_particular import RecoleccionParticular


class RecoleccionBase(SQLModel):
    fecha_inicio: datetime
    fecha_fin: datetime
    peso: float
    observaciones: str
    detalle: str
    vehiculo_id: UUID = Field(foreign_key="vehiculo.id")
    ruta_id: UUID = Field(foreign_key="ruta.id")
    tipo_residuo_id: UUID = Field(foreign_key="tiporesiduo.id")


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

    usuarios: 'Usuario' = Relationship(back_populates="recolecciones", link_model=UsuarioRecoleccion)

    vehiculo: Vehiculo = Relationship(back_populates="recolecciones")
    tipo_residuo: TipoResiduo = Relationship(back_populates="recolecciones")
    ruta: Ruta = Relationship(back_populates="recolecciones")
    recolecciones_particulares: list[RecoleccionParticular] = Relationship(back_populates="recoleccion")