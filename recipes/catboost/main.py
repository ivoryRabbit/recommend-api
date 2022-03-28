import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import roc_auc_score


df = pd.read_csv("data/ratings.csv")
df = df.assign(target=lambda df: np.where(df["rating"] > 3.0, 1, 0))
df = df.filter(items=["user_id", "item_id", "target"])

train_df, test_df = train_test_split(df, test_size=0.1)
train_df, valid_df = train_test_split(train_df, test_size=0.1)

X_train, y_train = train_df[["user_id", "item_id"]], train_df["target"]
X_valid, y_valid = valid_df[["user_id", "item_id"]], valid_df["target"]
X_test, y_test = test_df[["user_id", "item_id"]], test_df["target"]

model = CatBoostClassifier(iterations=100, random_state=123, learning_rate=0.01)
model.fit(
    X_train, y_train,
    cat_features=["user_id", "item_id"],
    eval_set=(X_valid, y_valid),
    metric_period=10,
    use_best_model=True,
)

y_pred = model.predict(X_test, prediction_type="Probability")

result = roc_auc_score(y_test.values, y_pred[:, 1])
