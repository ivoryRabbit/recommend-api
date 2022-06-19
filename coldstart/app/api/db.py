import os

from app.service.config import RedisConfig

redis = RedisConfig(
    host=os.environ["REDIS_HOST"],
    port=int(os.environ["REDIS_PORT"]),
    database="0"
)
