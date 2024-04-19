from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def get_todos():
    return "Hello world"
