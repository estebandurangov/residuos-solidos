from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import UUID

from app.model.usuario.usuario import UsuarioCreate, Usuario
from app.service.usuario.usuario import UsuarioService

from app.config.db import get_session

router = APIRouter()

tags = ["Usuario"]

@router.post("/create", tags=tags, response_model=Usuario, status_code=201)
def create(usuario: UsuarioCreate, db: Session = Depends(get_session)):
    usuario_db = UsuarioService(db).create(usuario)
    return usuario_db

@router.get("/all", tags=tags, response_model=list[Usuario])
def get_all(db: Session = Depends(get_session)):
    usuarios = UsuarioService(db).get_all()
    return usuarios