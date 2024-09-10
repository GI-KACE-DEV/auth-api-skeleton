from typing import Any
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.base_class import APIBase


# Define the association table
role_permissions = Table(
    'role_permissions',
    APIBase.metadata,
    Column('role_id', UUID(as_uuid=True), ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', UUID(as_uuid=True), ForeignKey('permissions.id'), primary_key=True)
)

class Role(APIBase):
    __tablename__ = 'roles'

    name = Column(String(255), unique=True, index=True)
    permissions = relationship(
        "Permission",
        secondary=role_permissions,
        back_populates="roles"
    )

class Permission(APIBase):
    __tablename__ = 'permissions'

    name = Column(String(255), unique=True, index=True)
    roles = relationship(
        "Role",
        secondary=role_permissions,
        back_populates="permissions"
    )