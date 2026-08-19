from src.infrastructure.database.base import Base
from src.roles.infrastructure.persistence.models.role import role_permissions_table


class RolePermissionModel(Base):
	__table__ = role_permissions_table