from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session


from app.model.ruta.ruta import RutaCreate, RutaUpdate, Ruta
from app.service.ruta.ruta import RutaService

from app.config.db import get_session

router = APIRouter()

tags = ["Ruta"]

@router.post("/create", tags=tags, response_model=Ruta, status_code=201)
def create(ruta: RutaCreate, db: Session = Depends(get_session)):
    ruta_db = RutaService(db).create(ruta)
    return ruta_db

@router.get("/all", tags=tags, response_model=list[Ruta], status_code=200)
def get_all(db: Session = Depends(get_session)):
    rutas = RutaService(db).get_all()
    return rutas