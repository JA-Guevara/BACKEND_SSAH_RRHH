from sqlalchemy import Column, String

from src.infrastructure.database.base import Base


class UserRoleModel(Base):
    __tablename__ = "user_roles"

    user_id = Column(String, primary_key=True)
    role_id = Column(String, primary_key=True)