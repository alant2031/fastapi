from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        extra = "forbid"


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {"item": "Do a simple task"}}


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        extra = "allow"
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"},
                ]
            }
        }
