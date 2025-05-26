from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1) Path 변수
@app.get("/items/{item_id}")
def get_item_handler(item_id: int):
    return {"message": item_id}


# 2) Query Parameter
@app.get("/items")
def get_items_handler(max_price: int = 0, category: str = ""):
    if category:
        return {
            "message": {
                "category": category,
                "max_price": max_price,
            }
        }

    return {
        "message": {
            "max_price": max_price,
        }
    }

# 3) Request Body
class ItemCreateRequest(BaseModel):
    name: str
    price: float


@app.post("/items")
def create_item_handler(body: ItemCreateRequest):
    return {"name": body.name, "price": body.price}
