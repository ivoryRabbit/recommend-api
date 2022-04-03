from typing import List
from pydantic import BaseModel, Field, validator


class UserIn(BaseModel):
    user_id: int
    gender: str
    age: int

    @classmethod
    @validator("user_id")
    def valid_id(cls, user_id):
        assert user_id.digit(), "Must be numerical"

    @classmethod
    @validator("gender")
    def valid_gender(cls, gender):
        assert gender in ["M", "F"], "Male or Female"

    @classmethod
    @validator("age")
    def valid_age(cls, age):
        assert age > 0, "Must be positive integer"


class RecommendOut(BaseModel):
    user_id: int
    item_ids: List[int] = Field(default_factory=list, title="Movie IDs")
