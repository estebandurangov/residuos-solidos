from fastapi import APIRouter

router = APIRouter()

#Recolección
from app.api.routes.recoleccion import recoleccion
from app.api.routes.recoleccion import recoleccion_particular
router.include_router(recoleccion.router, prefix="/recoleccion", tags=["Recolección"])
router.include_router(recoleccion_particular.router, prefix="/recoleccion_particular", tags=["Recolección Particular"])

#Barrido
from app.api.routes.barrido import barrido
router.include_router(barrido.router, prefix="/barrido", tags=["Barrido"])

#Usuario
from app.api.routes.usuario import usuario
router.include_router(usuario.router, prefix="/usuario", tags=["Usuario"])
from app.api.routes.usuario import user
router.include_router(user.router, prefix="/user", tags=["User"])

#Ruta
from app.api.routes.ruta import ruta
router.include_router(ruta.router, prefix="/ruta", tags=["Ruta"])

#TipoResiduo
from app.api.routes.tipoResiduo import tipoResiduo
router.include_router(tipoResiduo.router, prefix="/tipo_residuo", tags=["TipoResiduo"])

#Vehiculo
from app.api.routes.recoleccion import vehiculo
router.include_router(vehiculo.router, prefix="/vehiculo", tags=["Vehiculo"])
