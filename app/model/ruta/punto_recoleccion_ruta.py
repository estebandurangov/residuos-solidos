from uuid import UUID
from sqlmodel import Field, SQLModel

class PuntoRecoleccionRuta(SQLModel, table=True):
    ruta_id: UUID = Field(default=None, foreign_key="ruta.id", primary_key=True)
    punto_recoleccion_id: UUID = Field(default=None, foreign_key="puntorecoleccion.id", primary_key=True)
