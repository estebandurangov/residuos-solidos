from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, Optional
from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.residuo.tipo_residuo import TipoResiduo

class ResiduoBase(SQLModel):
    categoria: str
    descripcion: str
    observacion: str

class ResiduoCreate(ResiduoBase):
    pass

class ResiduoUpdate(ResiduoBase):
    categoria: str | None = None
    descripcion: str | None = None
    observacion: str | None = None

class Residuo(TableBase, ResiduoBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    tipos_residuos: list['TipoResiduo'] = Relationship(back_populates="residuo")