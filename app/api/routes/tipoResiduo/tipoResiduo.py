from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import UUID

from app.model.residuo.tipo_residuo import TipoResiduoCreate, TipoResiduoUpdate, TipoResiduo
from app.service.residuo.tipo_residuo import TipoResiduoService

from app.config.db import get_session

router = APIRouter()

tags = ["TipoResiduo"]

@router.post("/create", tags=tags, response_model=TipoResiduo, status_code=201)
def create(tipo_residuo: TipoResiduoCreate, db: Session = Depends(get_session)):
    tipo_residuo_db = TipoResiduoService(db).create(tipo_residuo)
    return tipo_residuo_db

@router.get("/all", tags=tags, response_model=list[TipoResiduo], status_code=200)
def get_all(db: Session = Depends(get_session)):
    tipos_residuos = TipoResiduoService(db).get_all()
    return tipos_residuos

@router.get("/{tipo_residuo_id}", tags=tags, response_model=TipoResiduo)
def get_by_id(tipo_residuo_id: UUID, db: Session = Depends(get_session)):
    tipo_residuo = TipoResiduoService(db).get_by_id(tipo_residuo_id)
    if not tipo_residuo:
        return JSONResponse(status_code=404, content={"message": "TipoResiduo not found"})
    return TipoResiduo.model_validate(tipo_residuo)