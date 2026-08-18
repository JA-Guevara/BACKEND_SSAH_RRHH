from datetime import datetime

from pydantic import BaseModel


class AuditLogResponse(BaseModel):
    id: str
    action: str
    description: str
    created_at: datetime
    user_id: str | None = None
