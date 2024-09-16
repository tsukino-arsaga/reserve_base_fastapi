from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    x: int
    y: int

app = FastAPI()

@app.get("/")
def index():
    return {"message":"hello Deta!"}

@app.post("/")
def calc(data: Data):
    z = data.x * data.y
    return {"result": z}