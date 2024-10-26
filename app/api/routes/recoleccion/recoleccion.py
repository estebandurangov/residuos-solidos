from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import uuid4

from app.model.recoleccion import RecoleccionCreate, RecoleccionUpdate, Recoleccion

from app.config.db import get_session

router = APIRouter()

tags = ["Recolección"]

@router.post("/create", tags=tags, response_model=Recoleccion, status_code=201)
def create(recoleccion: RecoleccionCreate, session: Session = Depends(get_session)):
    recoleccion = Recoleccion.model_validate(recoleccion)
    recoleccion.id = uuid4()
    session.add(recoleccion)
    session.commit()
    session.refresh(recoleccion)
    return recoleccion