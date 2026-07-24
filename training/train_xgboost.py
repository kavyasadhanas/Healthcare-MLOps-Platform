import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# -----------------------------
# MLflow Experiment
# -----------------------------
mlflow.set_experiment("Healthcare-MLOps")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/sample_data.csv")

X = df[["age", "gender", "family_history"]]
y = df["risk"]

# -----------------------------
# Start MLflow Run
# -----------------------------
with mlflow.start_run():

    # Create Model
    model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )

    # Train Model
    model.fit(X, y)

    # Predictions
    predictions = model.predict(X)

    # Metrics
    accuracy = accuracy_score(y, predictions)
    precision = precision_score(y, predictions)
    recall = recall_score(y, predictions)

    # -----------------------------
    # Log Parameters
    # -----------------------------
    mlflow.log_param("Model", "XGBoost")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("learning_rate", 0.1)
    mlflow.log_param("max_depth", 3)
    mlflow.log_param("random_state", 42)

    # -----------------------------
    # Log Metrics
    # -----------------------------
    mlflow.log_metric("Accuracy", accuracy)
    mlflow.log_metric("Precision", precision)
    mlflow.log_metric("Recall", recall)

    # -----------------------------
    # Save Model
    # -----------------------------
    joblib.dump(model, "models/risk_model.pkl")

    # Log model in MLflow
    mlflow.sklearn.log_model(model, "risk_model")

    print("===================================")
    print("XGBoost model trained successfully!")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print("Model saved to models/risk_model.pkl")
    print("Logged successfully in MLflow")
    print("===================================")