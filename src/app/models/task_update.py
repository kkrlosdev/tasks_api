from pydantic import BaseModel

class TaskUpdate(BaseModel):
    id: int
    name: str
    begin_date: str
    end_date: str
    short_description: str | None
    long_description: str | None
    status: int