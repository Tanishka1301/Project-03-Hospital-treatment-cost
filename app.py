import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Hospital Patient Cost Prediction",
    page_icon="🏥",
    layout="centered"
)

# Load Model
pipe = pickle.load(open("pipe.pkl", "rb"))

st.title("🏥 Hospital Patient Cost Prediction")
st.write("Predict the estimated hospital treatment cost based on patient information.")

# ---------------- INPUTS ----------------

age = st.number_input("Age", 18, 100, 25)

sex = st.selectbox(
    "Gender",
    ["male", "female"]
)

bmi = st.number_input(
    "BMI",
    10.0,
    60.0,
    25.0
)

children = st.number_input(
    "Number of Children",
    0,
    10,
    0
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

# ---------------- PREDICTION ----------------

if st.button("Predict Cost"):

    input_df = pd.DataFrame(
        [[age, sex, bmi, children, smoker, region]],
        columns=[
            "age",
            "sex",
            "bmi",
            "children",
            "smoker",
            "region"
        ]
    )

    result = pipe.predict(input_df)

    st.success("Prediction Completed Successfully!")

    st.subheader("📋 Patient Summary")

    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {sex}")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Children:** {children}")
    st.write(f"**Smoker:** {smoker}")
    st.write(f"**Region:** {region}")

    # BMI Category
    st.subheader("⚖ BMI Category")

    if bmi < 18.5:
        st.info("Underweight")
    elif bmi < 25:
        st.success("Normal Weight")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")

    # Prediction
    st.subheader("💰 Estimated Hospital Cost")

    st.metric(
        label="Predicted Cost",
        value=f"₹ {result[0]:,.2f}"
    )

    # Risk Level
    st.subheader("📈 Cost Level")

    if result[0] < 10000:
        st.success("🟢 Low Cost")

    elif result[0] < 30000:
        st.warning("🟡 Medium Cost")

    else:
        st.error("🔴 High Cost")

    # Health Tips
    st.subheader("❤️ Health Tips")

    if smoker == "yes":
        st.warning("Quit smoking to reduce future medical expenses.")

    if bmi >= 30:
        st.warning("Maintain a healthy weight through diet and exercise.")

    if bmi < 18.5:
        st.info("Consult a doctor for a healthy weight gain plan.")

    if smoker == "no" and 18.5 <= bmi < 25:
        st.success("Great! You are maintaining healthy habits.")

    st.balloons()
