
import streamlit as st
import pickle
import pandas as pd


# Page Settings

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)


# Load Model

model = pickle.load(open("model.pkl","rb"))



# Simple CSS

st.markdown("""
<style>

.title{
text-align:center;
color:#0066cc;
font-size:40px;
font-weight:bold;
}

.box{
padding:15px;
border-radius:10px;
background:#f5f5f5;
}

</style>
""", unsafe_allow_html=True)



# Title

st.markdown(
"""
<div class="title">
🩺 Diabetes Prediction System
</div>
""",
unsafe_allow_html=True
)


st.write(
"Machine Learning based diabetes risk prediction application"
)


st.divider()



# Input Section


st.subheader("👤 Patient Information")


col1,col2 = st.columns(2)



with col1:

    gender = st.selectbox(
        "Gender",
        ["Female","Male","Other"]
    )


    age = st.number_input(
        "Age",
        1,
        120,
        30
    )


    hypertension = st.selectbox(
        "Hypertension",
        [0,1]
    )


    heart_disease = st.selectbox(
        "Heart Disease",
        [0,1]
    )



with col2:

    smoking = st.selectbox(
        "Smoking History",
        [
        "never",
        "former",
        "current",
        "ever",
        "not current"
        ]
    )


    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        25.0
    )


    hba1c_level = st.number_input(
        "HbA1c Level",
        3.0,
        15.0,
        5.5
    )


    blood_glucose_level = st.number_input(
        "Blood Glucose Level",
        50,
        300,
        100
    )



st.write("")



# Prediction


if st.button(
    "🔍 Predict Diabetes",
    use_container_width=True
):


    # Encoding

    gender_Female = 1 if gender=="Female" else 0
    gender_Male = 1 if gender=="Male" else 0
    gender_Other = 1 if gender=="Other" else 0


    smoking_current = 1 if smoking=="current" else 0
    smoking_ever = 1 if smoking=="ever" else 0
    smoking_former = 1 if smoking=="former" else 0
    smoking_never = 1 if smoking=="never" else 0
    smoking_not_current = 1 if smoking=="not current" else 0



    data = pd.DataFrame(

        [[
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
        smoking_not_current
        ]],


        columns=[

        "age",
        "hypertension",
        "heart_disease",
        "bmi",
        "HbA1c_level",
        "blood_glucose_level",
        "gender_Female",
        "gender_Male",
        "gender_Other",
        "smoking_history_current",
        "smoking_history_ever",
        "smoking_history_former",
        "smoking_history_never",
        "smoking_history_not current"

        ]

    )



    prediction = model.predict(data)



    st.divider()



    # Result


    st.subheader("📊 Prediction Result")



    if prediction[0]==1:

        st.error(
            "⚠ Patient is Diabetic"
        )

        st.warning(
            "Consult doctor and maintain healthy lifestyle."
        )


    else:

        st.success(
            "✅ Patient is Not Diabetic"
        )

        st.info(
            "Maintain regular exercise and balanced diet."
        )



    # Patient Summary


    st.subheader("📋 Patient Summary")


    summary = pd.DataFrame({

        "Feature":[
            "Age",
            "BMI",
            "HbA1c Level",
            "Blood Glucose",
            "Smoking"
        ],

        "Value":[
            age,
            bmi,
            hba1c_level,
            blood_glucose_level,
            smoking
        ]

    })


    st.table(summary)



    # Download Report


    st.download_button(

        "📥 Download Report",

        summary.to_csv(index=False),

        file_name="Diabetes_Report.csv",

        mime="text/csv"

    )



st.divider()


st.caption(
"❤️ Diabetes Prediction App | Built with Streamlit & Machine Learning"
)
