from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship

from app.model.table_base import TableBase

from app.model.barrido.usuario_barrido import UsuarioBarrido

if TYPE_CHECKING:
    from app.model.usuario.usuario import Usuario
    from app.model.residuo.tipo_residuo import TipoResiduo
    from app.model.ruta.ruta import Ruta

class BarridoBase(SQLModel):
    fecha_inicio: datetime
    fecha_fin: datetime
    peso: float
    observacion: str
    detalle: str
    ruta_id: UUID = Field(foreign_key="ruta.id")
    tipo_residuo_id: UUID = Field(foreign_key="tiporesiduo.id")

class BarridoCreate(BarridoBase):
    pass

class BarridoUpdate(BarridoBase):
    fecha_inicio: datetime | None = None
    fecha_fin: datetime | None = None
    peso: float | None = None
    observacion: str | None = None
    detalle: str | None = None
    ruta_id: UUID | None = None
    tipo_residuo_id: UUID | None = None

class Barrido(TableBase, BarridoBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    usuarios: 'Usuario' = Relationship(back_populates="barridos", link_model=UsuarioBarrido)
    tipo_residuo: 'TipoResiduo' = Relationship(back_populates="barridos")
    ruta: 'Ruta' = Relationship(back_populates="barridos")
    