from fastapi import APIRouter

from app.api.routes.recoleccion import recoleccion

router = APIRouter()

router.include_router(recoleccion.router, prefix="/recoleccion", tags=["Recolección"])