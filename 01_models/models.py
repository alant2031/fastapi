from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        extra = "forbid"


class TodoItem(BaseModel):
    item: str

    class Config:
        extra = "forbid"
        schema_extra = {"example": {"item": "Do a simple task"}}
