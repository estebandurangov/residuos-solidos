from fastapi import APIRouter

from app.api.routes.recoleccion import recoleccion
from app.api.routes.usuario import user

router = APIRouter()

router.include_router(recoleccion.router, prefix="/recoleccion", tags=["Recolección"])
router.include_router(user.router, prefix="/user", tags=["Usuario"])
