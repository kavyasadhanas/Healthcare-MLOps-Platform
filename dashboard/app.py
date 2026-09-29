import streamlit as st
import requests

st.set_page_config(
    page_title="Healthcare Risk Prediction",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Healthcare Risk Prediction")

st.write("Enter patient details")

age = st.number_input("Age", 1, 120, 35)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
glucose = st.number_input("Glucose", 50, 300, 100)

if st.button("Predict"):

    payload = {
        "age": age,
        "bmi": bmi,
        "glucose": glucose
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            st.success("Prediction Successful")
            st.json(response.json())
        else:
            st.error(response.text)

    except Exception as e:
        st.error(str(e))