from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, Optional
from app.model.table_base import TableBase

if TYPE_CHECKING:
    from app.model.recoleccion.recoleccion import Recoleccion
    from app.model.barrido.barrido import Barrido

class TipoResiduoBase(SQLModel):
    nombre: str

class TipoResiduoCreate(TipoResiduoBase):
    pass

class TipoResiduoUpdate(TipoResiduoBase):
    nombre: Optional[str] = None

class TipoResiduo(TableBase, TipoResiduoBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    recolecciones: list["Recoleccion"] = Relationship(back_populates="tipo_residuo")
    barridos: list["Barrido"] = Relationship(back_populates="tipo_residuo")