# Diabetes Prediction Web App

A **Streamlit web application** that predicts the likelihood of diabetes based on patient health data using a trained **K-Nearest Neighbors (KNN)** model. This app demonstrates a complete workflow from ML model training to deployment.

## Features

- Predicts diabetes using inputs like:
  - Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- Real-time interactive predictions with Streamlit
- Easy-to-use interface suitable for demonstration or education
- Includes edge-case tests for borderline patients

## Demo

![App Screenshot](screenshot.png)  
_Live app_: [Streamlit Deployment Link](https://share.streamlit.io/yourusername/diabetes_app/main/app.py)

## Getting Started

### Prerequisites

- Python 3.10+
- Streamlit
- scikit-learn
- NumPy, Pandas
- joblib

### Install and Run Locally

```bash
git clone https://github.com/chaimaHarzali/diabetes_app.git
cd diabetes_app
python -m venv venv
# Activate venv:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
