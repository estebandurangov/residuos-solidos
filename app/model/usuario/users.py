from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from uuid import UUID
from typing import TYPE_CHECKING, Optional
from pydantic import conint

from app.model.usuario.usuario import Usuario

class Users(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}  # Especificar el esquema

    instance_id: Optional[UUID] = Field(default=None)
    id: UUID = Field(primary_key=True)
    aud: Optional[str] = Field(max_length=255)
    role: Optional[str] = Field(max_length=255)
    email: Optional[str] = Field(max_length=255, index=True)
    encrypted_password: Optional[str] = Field(max_length=255)
    email_confirmed_at: Optional[datetime]
    invited_at: Optional[datetime]
    confirmation_token: Optional[str] = Field(max_length=255, unique=True)
    confirmation_sent_at: Optional[datetime]
    recovery_token: Optional[str] = Field(max_length=255, unique=True)
    recovery_sent_at: Optional[datetime]
    email_change_token_new: Optional[str] = Field(max_length=255, unique=True)
    email_change: Optional[str] = Field(max_length=255)
    email_change_sent_at: Optional[datetime]
    last_sign_in_at: Optional[datetime]
    raw_app_meta_data: str | None= Field(sa_column=Field(JSONB)) # JSONB field
    raw_user_meta_data: str | None = Field(sa_column=Field(JSONB)) # JSONB field
    is_super_admin: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    phone: Optional[str] = Field(default=None)
    phone_confirmed_at: Optional[datetime]
    phone_change: Optional[str] = Field(default="")
    phone_change_token: Optional[str] = Field(default="")
    phone_change_sent_at: Optional[datetime]
    confirmed_at: Optional[datetime]
    email_change_token_current: Optional[str] = Field(default="")
    email_change_confirm_status: int = Field(default=0)
    banned_until: Optional[datetime]
    reauthentication_token: Optional[str] = Field(default="")
    reauthentication_sent_at: Optional[datetime]
    is_sso_user: bool = Field(default=False)
    deleted_at: Optional[datetime]
    is_anonymous: bool = Field(default=False)

    usuario: "Usuario" = Relationship(back_populates="user")

    # Configuración para permitir tipos arbitrarios
    class Config:
        arbitrary_types_allowed = True


class UserBase(SQLModel):
    id: UUID
    email: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    pass

class UserUpdate(UserBase):
    email: str | None = None

