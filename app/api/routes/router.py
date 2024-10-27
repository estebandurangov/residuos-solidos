from fastapi import APIRouter

from app.api.routes.recoleccion import recoleccion
from app.api.routes.usuario import user

router = APIRouter()

#Recolección
from app.api.routes.recoleccion import recoleccion_particular
router.include_router(recoleccion.router, prefix="/recoleccion", tags=["Recolección"])
router.include_router(recoleccion_particular.router, prefix="/recoleccion", tags=["Recolección"])
router.include_router(user.router, prefix="/user", tags=["user"])

#Ruta
from app.api.routes.ruta import ruta
router.include_router(ruta.router, prefix="/ruta", tags=["Ruta"])