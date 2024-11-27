from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from uuid import uuid4

from app.model.usuario.users import UserCreate, Users
from app.service.usuario.user import UserService

from app.config.db import get_session

router = APIRouter()

tags = ["User"]

@router.post("/create", response_model=Users, tags=tags, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    user_db = UserService(db).create(user)
    return user_db

@router.get("/all", response_model=list[Users], tags=tags)
def get_all(db: Session = Depends(get_session)):
    users = UserService(db).get_all()
    return users