from pandas import DataFrame
from typing import NewType, Dict

Item = NewType("Item", int)


class BestSeller:
    _pop_items: Dict[Item, int] | None = None

    def __init__(self, threshold: float = 3.0):
        self.threshold = threshold

    def fit(self, train_df: DataFrame) -> None:
        pop_item_df = (
            train_df
            .query(f"rating >= {self.threshold}")
            .groupby("item_id")["user_id"]
            .count()
            .sort_values(ascending=False)
        )

        self._pop_items = pop_item_df.to_dict()

    def get_pop_items(self) -> Dict[Item, int]:
        if self._pop_items is None:
            raise Exception("Model doesn't trained yet")

        return self._pop_items
