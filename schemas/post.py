from datetime import datetime

from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    content: str
    publiched_at: datetime | None = None
    published: bool = False
