from fastapi import FastAPI

from app.api.router import bestseller
from app.src import load_data, upload_data


app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs"
)
app.include_router(bestseller, prefix="/api/v1", tags=["bestseller"])


@app.on_event("startup")
async def startup():
    load_data(root_dir="data")
    upload_data(source_dir="data/ratings.csv")


@app.on_event("shutdown")
async def shutdown():
    pass

