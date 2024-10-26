from sqlmodel import SQLModel, Field
from datetime import datetime

from uuid import uuid4, UUID

class TableBase(SQLModel, table=True):
    id: UUID | None = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default=datetime.now(datetime.timezone.utc))
    updated_at: datetime = Field(default=datetime.now(datetime.timezone.utc))