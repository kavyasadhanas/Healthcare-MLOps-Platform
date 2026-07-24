import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="GenomicTwinOps", layout="wide")

st.title("🧬 GenomicTwinOps")
st.subheader("Disease Risk Prediction")

# -------------------------
# Input
# -------------------------

age = st.number_input("Age", 1, 100)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

family = st.selectbox(
    "Family History",
    ["No", "Yes"]
)

gender_value = 0 if gender == "Female" else 1
family_value = 0 if family == "No" else 1

# -------------------------
# Prediction
# -------------------------

if st.button("Predict"):

    payload = {
        "age": age,
        "gender": gender_value,
        "family_history": family_value
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict-risk",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction Complete")

            st.metric(
                "Predicted Risk",
                result["predicted_risk"]
            )

            st.metric(
                "Confidence",
                f'{result["confidence"]}%'
            )

        else:
            st.error(response.text)

    except Exception as e:
        st.error(e)

# -------------------------
# History
# -------------------------

st.divider()

st.subheader("Prediction History")

try:

    history = requests.get(
        "http://127.0.0.1:8000/history"
    )

    if history.status_code == 200:

        df = pd.DataFrame(history.json())

        st.dataframe(
            df,
            use_container_width=True
        )

except:
    st.warning("Backend not running")