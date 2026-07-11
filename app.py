import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.title("Hospital  Patient Cost Prediction App")

pipe = pickle.load(open("pipe.pkl", "rb+"))
df = pd.read_csv("cleaned_data.csv")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)

sex = st.selectbox("Sex", ["male", "female"])

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

children = st.number_input("Children", min_value=0, max_value=10, value=0)

smoker = st.selectbox("Smoker", ["yes", "no"])

region = st.selectbox("Region",
                      ["southwest", "southeast", "northwest", "northeast"])

# Prediction
if st.button("Predict Cost"):

    st.write("You have selected:")
    st.write(f"Age: {age}") 
    st.write(f"Sex: {sex}")
    st.write(f"BMI: {bmi}")
    st.write(f"Children : {children}")
    st.write(f"Smoker : {smoker}")
    st.write(f"Region : {region}")
    myinput = [[age, sex, bmi, children, smoker, region]]
    columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    myinput = pd.DataFrame(data = myinput, columns = columns)
    result = pipe.predict(myinput)
print("Predicted charges is :", round(result[0]))


if result[0] < 0:
        st.write("Sorry, the predicted charges is negative. Please check your input values.")
else:
        st.write("Predicted charges is:", str(round(result[0])))