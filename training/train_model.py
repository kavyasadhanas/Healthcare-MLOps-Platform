import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("data/sample_data.csv")

# Features
X = df[["age", "gender", "family_history"]]

# Target
y = df["risk"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "models/risk_model.pkl")

print("Model trained successfully!")
