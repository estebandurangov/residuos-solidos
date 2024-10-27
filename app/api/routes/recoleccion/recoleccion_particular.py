from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session

from app.model.recoleccion.recoleccion_particular import RecoleccionParticularCreate, RecoleccionParticularUpdate, RecoleccionParticular
from app.service.recoleccion.recoleccion_particular import RecoleccionParticularService

from app.config.db import get_session

router = APIRouter()

tags = ["Recolección"]

@router.post("/create", tags=tags, response_model=RecoleccionParticular, status_code=201)
def create(recoleccion: RecoleccionParticularCreate, db: Session = Depends(get_session)):
    recoleccion_db = RecoleccionParticularService(db).create(recoleccion)
    return recoleccion_db

@router.get("/particular/all", tags=tags, response_model=list[RecoleccionParticular], status_code=200)
def get_all(db: Session = Depends(get_session)):
    recolecciones = RecoleccionParticularService(db).get_all()
    return recolecciones