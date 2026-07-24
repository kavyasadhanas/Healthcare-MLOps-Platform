import pandas as pd
import joblib

from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("data/sample_data.csv")

X = df[["age", "gender", "family_history"]]
y = df["risk"]

model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "models/risk_model.pkl")

print("XGBoost model trained successfully!")