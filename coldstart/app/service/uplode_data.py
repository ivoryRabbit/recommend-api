import os
import pandas as pd

from app.service.model import BestSeller
from app.service.config import Redis


def upload_data(source_dir: str):
    train_df = pd.read_csv(source_dir)

    model = BestSeller()
    model.fit(train_df)

    result = model.get_pop_items()

    connector = Redis(
        host=os.environ["REDIS_HOST"],
        port=int(os.environ["REDIS_PORT"]),
        decode_responses=True
    )
    connector.zadd("bestseller", result)
