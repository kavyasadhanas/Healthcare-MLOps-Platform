import mlflow

mlflow.set_experiment("GenomicTwinOps")

with mlflow.start_run():

    mlflow.log_param("Model", "XGBoost")

    mlflow.log_param("Features", 3)

    mlflow.log_metric("Accuracy", 0.95)

    mlflow.log_metric("Precision", 0.94)

    mlflow.log_metric("Recall", 0.93)

    print("MLflow logging completed.")