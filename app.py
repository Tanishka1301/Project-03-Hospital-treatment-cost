import streamlit as st
import pickle
import pandas as pd




model = pickle.load(open("model.pkl", "rb"))

st.title("Diabetes Prediction System")

# User Input
gender = st.selectbox("Gender", ["Female", "Male", "Other"])
age = st.number_input("Age", min_value=1, max_value=120, value=30)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
smoking = st.selectbox(
    "Smoking History",
    [ "never", "former", "current", "ever", "not current"]
)
bmi = st.number_input("BMI", value=25.0)
hba1c_level = st.number_input("HbA1c Level", value=5.5)
blood_glucose_level = st.number_input("Blood Glucose Level", value=100)

# Prediction
if st.button("Predict"):

    # One-Hot Encoding
    gender_Female = 1 if gender == "Female" else 0
    gender_Male = 1 if gender == "Male" else 0
    gender_Other = 1 if gender.lower() == "other" else 0
    smoking_current = 1 if smoking == "current" else 0
    smoking_ever = 1 if smoking == "ever" else 0
    smoking_former = 1 if smoking == "former" else 0
    smoking_never = 1 if smoking == "never" else 0
    smoking_not_current = 1 if smoking == "not current" else 0
    
    data = pd.DataFrame([[
        age,
        hypertension,
        heart_disease,
        bmi,
        hba1c_level,
        blood_glucose_level,
        gender_Female,
        gender_Male,
        gender_Other,
        smoking_current,
        smoking_ever,
        smoking_former,
        smoking_never,
        smoking_not_current,
    ]], columns=[
        'age',
        'hypertension',
        'heart_disease',
        'bmi',
        'HbA1c_level',
        'blood_glucose_level',
        'gender_Female',
        'gender_Male',
        'gender_Other',
        'smoking_history_current',
        'smoking_history_ever',
        'smoking_history_former',
        'smoking_history_never',
        'smoking_history_not current',
        
    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Patient is Diabetic")
    else:
        st.success("Patient is Not Diabetic")
