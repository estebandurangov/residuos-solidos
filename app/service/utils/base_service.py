from datetime import datetime
from fastapi import HTTPException
from sqlmodel import SQLModel, select
from typing import Type, Optional
from uuid import uuid4

class BaseService:
    def __init__(self, db, model: Type[SQLModel]):
        self.db = db
        self.model = model

    def create(self, create_schema):
        try:
            with self.db:
                entity = self.model.model_validate(create_schema)
                entity.created_at = datetime.now()
                entity.updated_at = datetime.now()
                self.db.add(entity)
                self.db.commit()
                self.db.refresh(entity)
                return entity
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_all(self) -> list[SQLModel]:
        with self.db:
            entities = self.db.exec(select(self.model)).all()
            return entities

    def get_by_id(self, entity_id: str):
        entity = self.db.get(self.model, entity_id)
        if not entity:
            raise HTTPException(status_code=404, detail="Entity not found")
        return entity

    def update(self, entity_id: str, update_schema):
        with self.db as session:
            entity = session.get(self.model, entity_id)
            if not entity:
                raise HTTPException(status_code=404, detail="Entity not found")
            update_data = update_schema.model_dump(exclude_unset=True)
            entity.sqlmodel_update(update_data)
            entity.created_at = datetime.now()
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity

    def delete(self, entity_id: str):
        with self.db as session:
            entity = session.get(self.model, entity_id)
            if not entity:
                raise HTTPException(status_code=404, detail="Entity not found")
            session.delete(entity)
            session.commit()
            return {"ok": True}

