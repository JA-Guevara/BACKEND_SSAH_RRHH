from pydantic import BaseModel, Field


class AssignPermissionsRequest(BaseModel):
    permission_ids: list[str] = Field(min_length=1)