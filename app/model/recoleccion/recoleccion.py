from typing import TYPE_CHECKING, ClassVar
from uuid import UUID, uuid4
from app.model.table_base import TableBase
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

from app.model.recoleccion.usuario_recoleccion import UsuarioRecoleccion

if TYPE_CHECKING:
    from app.model.recoleccion.vehiculo import Vehiculo
    from app.model.residuo.tipo_residuo import TipoResiduo
    from app.model.usuario.usuario import Usuario
    from app.model.ruta.ruta import Ruta

from app.model.recoleccion.recoleccion_particular import RecoleccionParticular


class RecoleccionBase(SQLModel):
    fecha_inicio: datetime
    fecha_fin: datetime
    peso: float
    observacion: str
    detalle: str
    vehiculo_placa: str = Field(foreign_key="vehiculo.placa")
    ruta_id: UUID = Field(foreign_key="ruta.id")
    tipo_residuo_id: UUID = Field(foreign_key="tiporesiduo.id")


class RecoleccionCreate(RecoleccionBase):
    pass


class RecoleccionUpdate(RecoleccionBase):
    fecha_inicio: datetime | None = None
    fecha_fin: datetime | None = None
    peso: float | None = None
    observacion: str | None = None
    detalle: str | None = None
    vehiculo_placa: str | None = None
    ruta_id: UUID | None = None
    tipo_residuo_id: UUID | None = None


class Recoleccion(TableBase, RecoleccionBase, table=True):
    id: UUID | None = Field(primary_key=True, default_factory=uuid4)
    usuarios: list['Usuario'] = Relationship(back_populates="recolecciones", link_model=UsuarioRecoleccion)
    vehiculo: 'Vehiculo' = Relationship(back_populates="recolecciones")
    tipo_residuo: 'TipoResiduo' = Relationship(back_populates="recolecciones")
    ruta: 'Ruta' = Relationship(back_populates="recolecciones")
    recolecciones_particulares: list[RecoleccionParticular] = Relationship(back_populates="recoleccion")


class RecoleccionRead(RecoleccionBase):
    id: UUID


from app.model.residuo.tipo_residuo import TipoResiduoRead
from app.model.ruta.ruta import RutaRead
from app.model.usuario.usuario import UsuarioRead
from app.model.recoleccion.vehiculo import VehiculoRead


class RecoleccionWithData(RecoleccionRead):
    tipo_residuo: TipoResiduoRead
    ruta: RutaRead
    vehiculo: VehiculoRead
    usuarios: list[UsuarioRead] = []
