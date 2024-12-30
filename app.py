import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the instances that were created

with open('model.pkl','rb') as file:
    model = pickle.load(file)

with open('encoder.pkl','rb') as file:
    encoder = pickle.load(file)

def prediction(input_data):
    pca_data = encoder.transform(input_data)

    pred = model.predict(pca_data)[0]
    '''{
    0: 'Insufficient_Weight',
    1: 'Normal_Weight',
    2: 'Obesity_Type_I',
    3: 'Obesity_Type_II',
    4: 'Obesity_Type_III',
    5: 'Overweight_Level_I',
    6: 'Overweight_Level_II'
    }'''
    if pred==0:
        return 'Insufficient_Weight'
    elif pred==1:
        return 'Normal_Weight'
    elif pred==2:
        return 'Obesity_Type_I'
    elif pred==3:
        return 'Obesity_Type_II'
    elif pred==4:
        return 'Obesity_Type_III'
    elif pred==5:
        return 'Overweight_Level_I'
    else :
        return 'Overweight_Level_II'

def main():

    st.title('Fit Forecaster')
    st.subheader("FitForecaster is a prediction-focused application that uses AI to estimate \
                 an individual's risk of obesity based on input data. It provides quick and \
                 accurate predictions to help users understand potential risks.")

    # Input fields for each of the columns
    gender = st.selectbox('Enter Gender:', ['Male', 'Female'])
    age = st.number_input('Enter Age:', min_value=0, max_value=100, step=1)
    height = st.number_input('Enter Height (cm):', min_value=50, max_value=250, step=1)
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
    bmi = weight/(height/100)**2

    # Encode the categorical inputs using the LabelEncoder
    encoded_gender = encoder.fit_transform([gender])[0]  # Encoding 'Gender'
    encoded_family_history = encoder.fit_transform([family_history_with_overweight])[0]  # Encoding 'family_history_with_overweight'
    encoded_favc = encoder.fit_transform([favc])[0]  # Encoding 'FAVC'
    encoded_caec = encoder.fit_transform([caec])[0]  # Encoding 'CAEC'
    encoded_smoke = encoder.fit_transform([smoke])[0]  # Encoding 'SMOKE'
    encoded_scc = encoder.fit_transform([scc])[0]  # Encoding 'SCC'
    encoded_calc = encoder.fit_transform([calc])[0]  # Encoding 'CALC'
    encoded_mtrans = encoder.fit_transform([mtrans])[0]  # Encoding 'MTRANS'

    # Collect all the encoded inputs into a list
    input_list = [[encoded_gender, age, height, weight, encoded_family_history, encoded_favc, fcvc, ncp, encoded_caec,
               encoded_smoke, ch2o, encoded_scc, faf, tue, encoded_calc, encoded_mtrans, bmi]]

    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()

