from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, Optional
from app.model.table_base import TableBase

from app.model.barrido.barrido import Barrido

if TYPE_CHECKING:
    from app.model.recoleccion.recoleccion import Recoleccion

class TipoResiduoBase(SQLModel):
    categoria: str
    descripcion: str
    observacion: str

class TipoResiduoCreate(TipoResiduoBase):
    pass

class TipoResiduoUpdate(TipoResiduoBase):
    categoria: str | None = None
    descripcion: str | None = None
    observacion: str | None = None

class TipoResiduo(TableBase, TipoResiduoBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    recolecciones: list['Recoleccion'] = Relationship(back_populates="tipo_residuo")
    barridos: list[Barrido] = Relationship(back_populates="tipo_residuo")
    sub_tipos_residuo: list['SubTipoResiduo'] = Relationship(back_populates="tipo_residuo")