from pydantic import BaseModel, ConfigDict, Field


class PermissionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    resource: str
    action: str
    description: str | None = None


class RoleSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    description: str | None = None
    is_active: bool
    permissions: list[PermissionSchema] = Field(default_factory=list)