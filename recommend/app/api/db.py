import os

from databases import Database
from sqlalchemy.engine import create_engine
from sqlalchemy import (
    Table, MetaData, Column, Integer, String, ARRAY, Float, BigInteger
)

DATABASE_URI = os.environ["DATABASE_URI"]

engine = create_engine(DATABASE_URI)
database = Database(DATABASE_URI)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("gender", String(100)),
    Column("age", Integer),
    Column("occupation", Integer),
    Column("zip_code", Integer),
)

movies = Table(
    "movies",
    metadata,
    Column("item_id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("genres", ARRAY(String(50))),
)

ratings = Table(
    "ratings",
    metadata,
    Column("user_id", Integer),
    Column("item_id", Integer),
    Column("rating", Float),
    Column("timestamp", BigInteger),
)
