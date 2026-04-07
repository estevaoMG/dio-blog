from datetime import datetime

from pydantic import BaseModel


class PostOut(BaseModel):
    title: str
    content: str
    publiched_at: datetime | None
    date: datetime
