import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the model and encoder
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)  # Assuming it's a LabelEncoder or similar

def prediction(input_data):
    # Make prediction
    pred = model.predict(input_data)[0][0]

    # Return corresponding category
    categories = [
        'Insufficient_Weight', 'Normal_Weight', 'Obesity_Type_I', 
        'Obesity_Type_II', 'Obesity_Type_III', 'Overweight_Level_I', 
        'Overweight_Level_II'
    ]
    return categories[pred]

def main():
    st.title('Fit Forecaster')
    st.subheader("FitForecaster is a prediction-focused application that uses AI to estimate \
                 an individual's risk of obesity based on input data. It provides quick and \
                 accurate predictions to help users understand potential risks.")

    # Input fields for each of the columns
    gender = (lambda x : 0 if x.lower()=='male' else 1)(st.selectbox('Enter Gender:', ['Male', 'Female']))
    age = st.number_input('Enter Age:', min_value=0, max_value=100, step=1)
    height = st.number_input('Enter Height (cm):', min_value=50, max_value=300, step=1)
    weight = st.number_input('Enter Weight (kg):', min_value=1, max_value=200, step=1)
    family_history_with_overweight = st.selectbox('Family history with overweight:', ['Yes', 'No'])
    favc = st.selectbox('FAVC (Frequent consumption of high caloric food):', ['Yes', 'No'])
    fcvc = st.number_input('FCVC (Frequency of vegetables consumption per day):', min_value=0, max_value=10, step=1)
    ncp = st.number_input('NCP (Number of main meals per day):', min_value=0, max_value=10, step=1)
    caec = st.selectbox('CAEC (Consumption of food between meals):', ['No', 'Sometimes', 'Always'])
    smoke = st.selectbox('SMOKE (Do you smoke?):', ['Yes', 'No'])
    ch2o = st.number_input('CH2O (Consumption of water per day in liters):', min_value=0.1, max_value=10.0, step=0.1)
    scc = st.selectbox('SCC (Current physical activity level):', ['Low', 'Medium', 'High'])
    faf = st.number_input('FAF (Frequency of physical activity per week):', min_value=0, max_value=7, step=1)
    tue = st.number_input('TUE (Time spent on exercise or activity in hours per week):', min_value=0, max_value=168, step=1)
    calc = st.selectbox('CALC (Do you consume alcohol?):', ['Yes', 'No'])
    mtrans = st.selectbox('MTRANS (Transportation mode):', ['Walking', 'Bicycle', 'Car', 'Public transport'])
    bmi = weight / (height/100)**2  # Calculate BMI manually

    # Encode the categorical inputs using the LabelEncoder
    encoded_family_history = label_encoder.transform([family_history_with_overweight])[0]
    encoded_favc = label_encoder.transform([favc])[0]
    encoded_caec = label_encoder.transform([caec])[0]
    encoded_smoke = label_encoder.transform([smoke])[0]
    encoded_scc = label_encoder.transform([scc])[0]
    encoded_calc = label_encoder.transform([calc])[0]
    encoded_mtrans = label_encoder.transform([mtrans])[0]

    # Collect all the encoded inputs into a list
    input_list = [[gender, age, height, weight, encoded_family_history, encoded_favc, fcvc, ncp, 
                  encoded_caec, encoded_smoke, ch2o, encoded_scc, faf, tue, encoded_calc, encoded_mtrans, bmi]]

    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()
