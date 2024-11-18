from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import UUID

from app.model.recoleccion.recoleccion import RecoleccionCreate, RecoleccionUpdate, Recoleccion, RecoleccionWithData
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

@router.get("/{recoleccion_id}", tags=tags, response_model=RecoleccionWithData)
def get_by_id(recoleccion_id: UUID, db: Session = Depends(get_session)):
    recoleccion = RecoleccionService(db).get_by_id(recoleccion_id)
    if not recoleccion:
        return JSONResponse(status_code=404, content={"message": "Recolección not found"})
    return RecoleccionWithData.model_validate(recoleccion)

@router.put("/update/{recoleccion_id}", tags=tags, response_model=Recoleccion)
def update(recoleccion_id: UUID, recoleccion: RecoleccionUpdate, db: Session = Depends(get_session)):
    recoleccion_db = db.get(Recoleccion, recoleccion_id)
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
    recoleccion = RecoleccionService(db).delete(recoleccion_id)
    if not recoleccion:
        return JSONResponse(status_code=404, content={"message": "Recolección not found"})
    return {"ok": True}