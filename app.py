import streamlit as st
import joblib
import numpy as np

model = joblib.load("knn_diabetes_model.pkl")

st.title("Diabetes Prediction App")

st.write("Enter patient details below:")

Pregnancies = st.number_input("Pregnancies",0,20,1)
Glucose = st.number_input("Glucose", 0, 200, 120)
BloodPressure = st.number_input("BloodPressure", 0, 150, 70)
SkinThickness = st.number_input("SkinThickness", 0, 100, 20)
Insulin = st.number_input("Insulin", 0, 900, 79)
BMI = st.number_input("BMI", 0.0, 70.0, 25.0)
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", 0.0, 3.0, 0.5)
Age = st.number_input("Age", 0, 120, 33)

if st.button("predict") :
    X = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                   BMI, DiabetesPedigreeFunction, Age]])
    prediction = model.predict(X)[0]

    if prediction == 1 :
        st.error("The patient is likely diabetic")
    else : 
        st.success("The patient is likely NOT diabetic")
    