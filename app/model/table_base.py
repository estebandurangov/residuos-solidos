from sqlmodel import SQLModel, Field
from datetime import datetime

from uuid import uuid4, UUID

class TableBase(SQLModel):
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())