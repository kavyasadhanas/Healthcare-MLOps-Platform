import os
import joblib


class ModelRegistry:

    def __init__(self):
        self.models = {}
        self.versions = {}

    def register(self, name, path, version):

        if os.path.exists(path):
            self.models[name] = joblib.load(path)
            self.versions[name] = version
            print(f"{name} loaded.")
        else:
            print(f"{path} not found.")

    def get(self, name):
        return self.models.get(name)

    def version(self, name):
        return self.versions.get(name, "Unknown")


registry = ModelRegistry()

registry.register(
    "risk_model",
    "models/risk_model.pkl",
    "1.0"
)

registry.register(
    "forecast_model",
    "models/forecast_model.pkl",
    "1.0"
)

registry.register(
    "mutation_model",
    "models/mutation_model.pkl",
    "1.0"
)