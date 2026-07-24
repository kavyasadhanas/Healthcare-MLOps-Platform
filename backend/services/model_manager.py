import joblib
import os

MODEL_DIR = "models"


class ModelManager:

    def __init__(self):
        self.models = {}

    def load_model(self, name):

        path = os.path.join(
            MODEL_DIR,
            f"{name}.pkl"
        )

        self.models[name] = joblib.load(path)

    def get_model(self, name):
        return self.models.get(name)


model_manager = ModelManager()

# Load available models
try:
    model_manager.load_model("risk_model")
except:
    print("risk_model.pkl not found")

try:
    model_manager.load_model("forecast_model")
except:
    print("forecast_model.pkl not found")

try:
    model_manager.load_model("mutation_model")
except:
    print("mutation_model.pkl not found")