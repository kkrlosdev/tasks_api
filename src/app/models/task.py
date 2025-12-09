from pydantic import BaseModel

class Task(BaseModel):
    name: str
    begin_date: str
    end_date: str
    short_description: str | None
    long_description: str | None
    status: int