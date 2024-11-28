from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from uuid import UUID
from sqlalchemy import func
from sqlmodel import select

from app.model.barrido.barrido import BarridoCreate, BarridoUpdate, Barrido, BarridoWithData
from app.model.barrido.usuario_barrido import UsuarioBarrido
from app.model.residuo.tipo_residuo import TipoResiduo
from app.model.ruta.ruta import Ruta
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

@router.post("/{barrido_id}/assign_users", tags=tags, response_model=dict)
def assign_users_to_barrido(barrido_id: UUID, user_ids: list[UUID], db: Session = Depends(get_session)):
    barrido = db.get(Barrido, barrido_id)
    if not barrido:
        return JSONResponse(status_code=404, content={"message": "Barrido not found"})

    for user_id in user_ids:
        if user_id not in [user.id for user in barrido.usuarios]:
            usuario_barrido = UsuarioBarrido(barrido_id=barrido_id, usuario_id=user_id)
            db.add(usuario_barrido)

    db.commit()
    return {"message": "Users successfully assigned"}

@router.put("/{barrido_id}/update_users", tags=tags, response_model=dict)
def update_users_in_barrido(barrido_id: UUID, user_ids: list[UUID], db: Session = Depends(get_session)):
    barrido = db.get(Barrido, barrido_id)
    if not barrido:
        return JSONResponse(status_code=404, content={"message": "Barrido not found"})

    db.query(UsuarioBarrido).filter(UsuarioBarrido.barrido_id == barrido_id).delete()

    for user_id in user_ids:
        usuario_barrido = UsuarioBarrido(barrido_id=barrido_id, usuario_id=user_id)
        db.add(usuario_barrido)

    db.commit()
    return {"message": "Usuarios actualizados con éxito"}

@router.get("/stats/barridos-per-date", tags=tags, response_model=dict)
def get_barridos_per_month(db: Session = Depends(get_session)):
    query = (
        db.query(func.date_trunc('month', Barrido.fecha_inicio).label('month'), func.count(Barrido.id).label('total'))
        .group_by('month')
        .order_by('month')
    )
    results = query.all()
    return {"data": [{"date": result[0], "total": result[1]} for result in results]}

@router.get("/stats/barridos-kg-per-date", tags=tags, response_model=dict)
def get_barridos_kg_per_date(db: Session = Depends(get_session)):
    query = (
        db.query(func.date_trunc('month', Barrido.fecha_inicio).label('month'), func.sum(Barrido.peso).label('total'))
        .group_by('month')
        .order_by('month')
    )
    results = query.all()
    return {"data": [{"date": result[0], "total": result[1]} for result in results]}

@router.get("/stats/barridos-per-tipo-residuo", tags=tags, response_model=dict)
def get_barridos_per_tipo_residuo(db: Session = Depends(get_session)):
    query = (
        db.query(TipoResiduo.categoria, func.count(Barrido.id).label('total'))
        .join(TipoResiduo, Barrido.tipo_residuo_id == TipoResiduo.id)
        .group_by(TipoResiduo.categoria)
        .order_by('total')
    )
    results = query.all()
    return {"data": [{"type": result[0], "total": result[1]} for result in results]}

@router.get("/stats/barridos-per-ruta", tags=tags, response_model=dict)
def get_barridos_per_ruta(db: Session = Depends(get_session)):
    query = (
        db.query(Ruta.nombre, func.count(Barrido.id).label('total'))
        .join(Ruta, Barrido.ruta_id == Ruta.id)
        .group_by(Ruta.nombre)
        .order_by('total')
    )
    results = query.all()
    return {"data": [{"type": result[0], "total": result[1]} for result in results]}