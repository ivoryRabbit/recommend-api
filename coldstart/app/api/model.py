from sqlmodel import SQLModel
from typing import List


class Item(SQLModel):
    id: int


class ItemOut(SQLModel):
    item_ids: List[Item]


class EventInput(SQLModel):
    user_id: int
    item_id: int
    rating: float
    timestamp: int
