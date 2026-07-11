import streamlit as st
import pandas as pd
import pickle

# ---------------- Page ----------------

st.set_page_config(
    page_title="Hospital Patient Cost Prediction",
    page_icon="🏥",
    layout="wide"
)

# ---------------- Load Model ----------------

pipe = pickle.load(open("pipe.pkl", "rb"))

# ---------------- Sidebar ----------------

st.sidebar.title("🏥 Hospital Dashboard")

st.sidebar.success("Machine Learning Project")

st.sidebar.write("""
✔ Hospital Cost Prediction

✔ BMI Analysis

✔ Health Risk

✔ Patient Report
""")

# ---------------- Title ----------------

st.markdown(
"""
<h1 style='text-align:center;color:green;'>
🏥 Hospital Patient Cost Prediction
</h1>
""",
unsafe_allow_html=True
)

st.write("Predict the estimated hospital treatment cost using Machine Learning.")

st.markdown("---")

# ---------------- Inputs ----------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        18,
        100,
        25
    )

    sex = st.selectbox(
        "Gender",
        ["male","female"]
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        25.0
    )

with col2:

    children = st.number_input(
        "Children",
        0,
        10,
        0
    )

    smoker = st.selectbox(
        "Smoker",
        ["yes","no"]
    )

    region = st.selectbox(
        "Region",
        [
            "southwest",
            "southeast",
            "northwest",
            "northeast"
        ]
    )

# ---------------- Prediction ----------------

if st.button("Predict Cost"):

    input_df = pd.DataFrame(
        [[age,sex,bmi,children,smoker,region]],
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

    st.balloons()

    st.markdown("---")

    # Dashboard Cards

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Age",age)
    c2.metric("BMI",bmi)
    c3.metric("Children",children)
    c4.metric("Estimated Cost",f"₹ {result[0]:,.2f}")

    st.markdown("---")

    # Patient Summary

    st.subheader("📋 Patient Summary")

    summary = pd.DataFrame({
        "Feature":[
            "Age",
            "Gender",
            "BMI",
            "Children",
            "Smoker",
            "Region"
        ],
        "Value":[
            age,
            sex,
            bmi,
            children,
            smoker,
            region
        ]
    })

    st.table(summary)

    # BMI

    st.subheader("⚖ BMI Category")

    if bmi < 18.5:
        st.info("Underweight")

    elif bmi < 25:
        st.success("Normal")

    elif bmi < 30:
        st.warning("Overweight")

    else:
        st.error("Obese")

    # Smoker Status

    st.subheader("❤️ Health Status")

    if smoker == "yes":
        st.error("High Risk (Smoker)")
    else:
        st.success("Low Risk (Non-Smoker)")

    # Cost Meter

    st.subheader("📊 Estimated Cost Level")

    progress = min(int(result[0]/50000*100),100)

    st.progress(progress)

    # Health Tips

    st.subheader("💡 Health Tips")

    if smoker=="yes":
        st.warning("🚭 Stop smoking to reduce medical expenses.")

    if bmi>=30:
        st.warning("🥗 Maintain a healthy diet.")

    if age>60:
        st.info("🩺 Regular health check-ups are recommended.")

    if smoker=="no" and bmi<25:
        st.success("✅ Keep maintaining a healthy lifestyle.")

    # Doctor Advice

    st.subheader("👨‍⚕️ Doctor's Advice")

    st.info("""
• Exercise regularly

• Eat a balanced diet

• Drink enough water

• Get proper sleep

• Visit your doctor for regular check-ups
""")

    # Download Report

    report = summary.copy()

    report.loc[len(report)] = [
        "Predicted Cost",
        round(result[0],2)
    ]

    st.download_button(
        "📥 Download Report",
        report.to_csv(index=False),
        file_name="Hospital_Report.csv",
        mime="text/csv"
    )

st.markdown("---")

st.markdown(
"""
<center>
❤️ Developed using Streamlit & Machine Learning
</center>
""",
unsafe_allow_html=True
)lease check your input values.")
else:
        st.write("Predicted charges is:", str(round(result[0])))
