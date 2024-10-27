from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from uuid import uuid4

from app.model.usuario.users import UserBase, Users

from app.config.db import get_session

router = APIRouter()

tags = ["user"]

@router.get("/all", response_model=list[UserBase], tags=tags, status_code=200)
def get_all_users(session: Session = Depends(get_session)):
    with session as db:
        users = db.exec(select(Users)).all()
    return [UserBase.model_validate(user.model_dump()) for user in users] 