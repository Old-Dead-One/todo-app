from pydantic import BaseModel


class Todo(BaseModel):
    number: int
    description: str

