from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import UUID

from app.model.recoleccion.recoleccion_particular import RecoleccionParticularCreate, RecoleccionParticularUpdate, RecoleccionParticular
from app.service.recoleccion.recoleccion_particular import RecoleccionParticularService

from app.config.db import get_session

router = APIRouter()

tags = ["Recolección Particular"]

@router.post("/create", tags=tags, response_model=RecoleccionParticular, status_code=201)
def create(recoleccion: RecoleccionParticularCreate, db: Session = Depends(get_session)):
    recoleccion_db = RecoleccionParticularService(db).create(recoleccion)
    return recoleccion_db

@router.get("/all", tags=tags, response_model=list[RecoleccionParticular], status_code=200)
def get_all(db: Session = Depends(get_session)):
    recolecciones = RecoleccionParticularService(db).get_all()
    return recolecciones

@router.get("/{recoleccion_id}", tags=tags, response_model=RecoleccionParticular)
def get_by_id(recoleccion_id: UUID, db: Session = Depends(get_session)):
    recoleccion = RecoleccionParticularService(db).get_by_id(recoleccion_id)
    if not recoleccion:
        return JSONResponse(status_code=404, content={"message": "Recolección not found"})
    return recoleccion

@router.put("/update/{recoleccion_id}", tags=tags, response_model=RecoleccionParticular)
def update(recoleccion_id: UUID, recoleccion: RecoleccionParticularUpdate, db: Session = Depends(get_session)):
    recoleccion_db = db.get(RecoleccionParticular, recoleccion_id)
    if not recoleccion_db:
        return JSONResponse(status_code=404, content={"message": "Recolección not found"})

    for key, value in recoleccion.dict(exclude_unset=True).items():
        setattr(recoleccion_db, key, value)

    db.add(recoleccion_db)
    db.commit()
    db.refresh(recoleccion_db)
    return recoleccion_db

@router.delete("/delete/{recoleccion_id}", tags=tags, response_model=dict)
def delete(recoleccion_id: UUID, db: Session = Depends(get_session)):
    recoleccion = RecoleccionParticularService(db).delete(recoleccion_id)
    if not recoleccion:
        return JSONResponse(status_code=404, content={"message": "Recolección not found"})
    return {"ok": True}
