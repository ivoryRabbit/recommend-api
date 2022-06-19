from redis import Redis
from dataclasses import dataclass


@dataclass
class RedisConfig:
    host: str
    port: int
    database: str

    def connector(self) -> Redis:
        engine = Redis(host=self.host, port=self.port, decode_responses=True)
        return engine
