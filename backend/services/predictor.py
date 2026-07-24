from backend.services.model_registry import registry


def predict(age, gender, family_history):
    # Get the trained model
    model = registry.get("risk_model")

    if model is None:
        raise Exception("Risk model not loaded.")

    # Prepare input
    input_data = [[age, gender, family_history]]

    # Predict
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    # Convert NumPy values to Python types
    risk = int(prediction[0])
    confidence = float(round(float(max(probability[0])) * 100, 2))
    model_version = str(registry.version("risk_model"))

    return {
        "risk": risk,
        "confidence": confidence,
        "model_version": model_version
    }