from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
# uvicorn main:app --reload

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

app = FastAPI()

@app.post("/")
async def index(data: Data):
    return {"data": data}