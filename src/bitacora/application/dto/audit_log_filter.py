from pydantic import BaseModel


class AuditLogFilter(BaseModel):
    user_id: str | None = None
    action: str | None = None
    limit: int = 50
    offset: int = 0
