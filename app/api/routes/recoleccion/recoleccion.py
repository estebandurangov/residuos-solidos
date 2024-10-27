from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import uuid4

from app.model.recoleccion.recoleccion import RecoleccionCreate, RecoleccionUpdate, Recoleccion
from app.service.recoleccion.recoleccion import RecoleccionService

from app.config.db import get_session

router = APIRouter()

tags = ["Recolección"]

@router.post("/create", tags=tags, response_model=Recoleccion, status_code=201)
def create(recoleccion: RecoleccionCreate, db: Session = Depends(get_session)):
    recoleccion_db = RecoleccionService(db).create(recoleccion)
    return recoleccion_db

@router.get("/all", tags=tags, response_model=list[Recoleccion])
def get_all(db: Session = Depends(get_session)):
    recolecciones = RecoleccionService(db).get_all()
    return recolecciones