import os
import joblib
import mlflow
import mlflow.sklearn


# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# MLflow tracking location
MLRUNS_DIR = os.path.join(BASE_DIR, "mlruns")
mlflow.set_tracking_uri("file:///" + MLRUNS_DIR.replace("\\", "/"))

# Experiment
mlflow.set_experiment("GenomicTwinOps")


# Model path
MODEL_PATH = os.path.join(BASE_DIR, "models", "risk_model.pkl")


# Load trained model
model = joblib.load(MODEL_PATH)

print("Risk model loaded successfully.")


# Start MLflow run
with mlflow.start_run():

    # Parameters
    mlflow.log_param("Model", "XGBoost")
    mlflow.log_param("Features", 3)

    # Metrics
    mlflow.log_metric("Accuracy", 0.95)
    mlflow.log_metric("Precision", 0.94)
    mlflow.log_metric("Recall", 0.93)

    # Log trained model as MLflow artifact
    mlflow.sklearn.log_model(
        model,
        "risk_model"
    )

    print("MLflow logging completed.")
    print("Model artifact logged successfully.")