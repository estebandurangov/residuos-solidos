from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, Optional
from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.residuo.tipo_residuo import TipoResiduo

class SubTipoResiduoBase(SQLModel):
    categoria: str
    descripcion: str
    observacion: str
    tipo_residuo_id: UUID = Field(foreign_key="tiporesiduo.id")

class SubTipoResiduoCreate(SubTipoResiduoBase):
    pass

class SubTipoResiduoUpdate(SubTipoResiduoBase):
    categoria: str | None = None
    descripcion: str | None = None
    observacion: str | None = None

class SubTipoResiduo(TableBase, SubTipoResiduoBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    tipo_residuo: TipoResiduo = Relationship(back_populates="sub_tipos_residuo")