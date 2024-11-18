from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import UUID

from app.model.recoleccion.vehiculo import VehiculoCreate, VehiculoUpdate, Vehiculo
from app.service.recoleccion.vehiculo import VehiculoService

from app.config.db import get_session

router = APIRouter()

tags = ["Vehiculo"]


@router.post("/create", tags=tags, response_model=Vehiculo, status_code=201)
def create(vehiculo: VehiculoCreate, db: Session = Depends(get_session)):
    vehiculo_db = VehiculoService(db).create(vehiculo)
    return vehiculo_db


@router.get("/all", tags=tags, response_model=list[Vehiculo], status_code=200)
def get_all(db: Session = Depends(get_session)):
    vehiculos = VehiculoService(db).get_all()
    return vehiculos


@router.get("/{vehiculo_placa}", tags=tags, response_model=Vehiculo)
def get_by_id(vehiculo_placa: str, db: Session = Depends(get_session)):
    vehiculo = VehiculoService(db).get_by_id(vehiculo_placa)
    if not vehiculo:
        return JSONResponse(status_code=404, content={"message": "Vehiculo not found"})
    return Vehiculo.model_validate(vehiculo)