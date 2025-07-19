import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.image(r"c:\Users\pc\Downloads\diabetes.jpeg", caption="Diabetes Chart", use_column_width=True)
st.title("🩺 Diabetes Predictor App")

Pregnancies = st.number_input("Pregnancies", value=2)
Glucose = st.number_input("Glucose", value=148)
BloodPressure = st.number_input("BloodPressure", value=72)
SkinThickness = st.number_input("SkinThickness", value=35)
Insulin = st.number_input("Insulin", value=0)
BMI = st.number_input("BMI", value=33.6)
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", value=0.627)
Age = st.number_input("Age", value=50)

 
if st.button("🔍 Predict Diabetes"):
    try:
        with open('new2_Diabetes_model.pkl', 'rb') as f:
            model = pickle.load(f)

        
        x_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if hasattr(model, "predict"):
            prediction = model.predict(x_data)

            
            st.subheader('Does the preson have diabetes ?')
            if prediction[0] == 1:
                st.success(" Yes,most likely ✅")
            else:
                st.info(" No ,most likely ❌")
        else:
            st.error("❌")

    except Exception as e:
        st.error(f"erroe !!!: {e}")
