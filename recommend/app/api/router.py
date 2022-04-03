from fastapi import APIRouter, HTTPException

from app.api.model import UserIn, RecommendOut
from app.api.service import request_inference

recommend = APIRouter()


@recommend.get("/", response_model=RecommendOut)
async def get_inference(payload: UserIn):
    movie_ids = await request_inference(**payload.dict())
    if not movie_ids:
        raise HTTPException(status_code=404, detail="No recommended items")
    return movie_ids
