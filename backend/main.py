from fastapi import FastAPI

from models import Todo

app = FastAPI()

todo: list[Todo] = []


@app.get("/")
async def get_todos() -> list[Todo]:
    return todo

@app.post("/")
async def create_todo():
    return


