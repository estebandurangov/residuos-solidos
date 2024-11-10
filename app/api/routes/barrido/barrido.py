from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import UUID

from app.model.barrido.barrido import BarridoCreate, BarridoUpdate, Barrido, BarridoWithData
from app.service.barrido.barrido import BarridoService

from app.config.db import get_session

router = APIRouter()

tags = ["Barrido"]

@router.post("/create", tags=tags, response_model=Barrido, status_code=201)
def create(barrido: BarridoCreate, db: Session = Depends(get_session)):
    barrido_db = BarridoService(db).create(barrido)
    return barrido_db

@router.get("/all", tags=tags, response_model=list[Barrido])
def get_all(db: Session = Depends(get_session)):
    barridos = BarridoService(db).get_all()
    return barridos

@router.get("/{barrido_id}", tags=tags, response_model=BarridoWithData)
def get_by_id(barrido_id: UUID, db: Session = Depends(get_session)):
    barrido = BarridoService(db).get_by_id(barrido_id)
    if not barrido:
        return JSONResponse(status_code=404, content={"message": "Barrido not found"})
    return BarridoWithData.model_validate(barrido)

@router.put("/update/{barrido_id}", tags=tags, response_model=Barrido)
def update(barrido_id: UUID, barrido: BarridoUpdate, db: Session = Depends(get_session)):
    barrido_db = db.get(Barrido, barrido_id)
    if not barrido_db:
        return JSONResponse(status_code=404, content={"message": "Barrido not found"})

    for key, value in barrido.dict(exclude_unset=True).items():
        setattr(barrido_db, key, value)

    db.add(barrido_db)
    db.commit()
    db.refresh(barrido_db)
    return barrido_db

@router.delete("/delete/{barrido_id}", tags=tags, response_model=dict)
def delete(barrido_id: UUID, db: Session = Depends(get_session)):
    barrido = BarridoService(db).delete(barrido_id)
    if not barrido:
        return JSONResponse(status_code=404, content={"message": "Barrido not found"})
    return {"ok": True}