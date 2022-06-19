from fastapi import APIRouter

from app.api.db import redis
from app.api.model import ItemOut, EventInput

bestseller = APIRouter()
client = redis.connector()


@bestseller.get("/bestseller", response_model=ItemOut)
async def get_bestseller(top_k: int = 10):
    assert top_k > 0

    item_ids = client.zrevrange("bestseller", 0, top_k)
    return {"item_ids": [{"id": int(i)} for i in item_ids]}


@bestseller.post("/bestseller")
async def update_bestseller(event: EventInput):
    updated_score = client.zincrby("bestseller", 1, event.item_id)
    return updated_score
