import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the instances that were created

with open('model.pkl','rb') as file:
    model = pickle.load(file)

def prediction(input_data):
    pred = model.predict(input_data)
   
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
    st.subheader("FitForecaster is a prediction-focused application that uses Machine Learning Algorithm to estimate \
                 an individual's type of obesity based on input data.")

    # Input fields for each of the columns
    gender = (lambda x : 1 if x=='Male' else 0)(st.selectbox('Enter Gender:', ['Male', 'Female']))
    age = st.number_input('Enter Age:', min_value=0, max_value=100, step=1)
    height = st.number_input('Enter Height (cm):', min_value=50, max_value=300, step=1)
    weight = st.number_input('Enter Weight (kg):', min_value=1, max_value=200, step=1)
    family_history_with_overweight = (lambda x : 1 if x=='Yes' else 0)(st.selectbox('Family history with overweight:', ['Yes', 'No']))
    favc = (lambda x : 1 if x=='Yes' else 0)(st.selectbox('FAVC (Frequent consumption of high caloric food):', ['Yes', 'No']))
    fcvc = st.number_input('FCVC (Frequency of vegetables consumption per day):', min_value=0, max_value=10, step=1)
    ncp = st.number_input('NCP (Number of main meals per day):', min_value=0, max_value=10, step=1)
    caec = (lambda x : 0 if x=='Always' else 1 if x=='Frequently' else 3 if x=='No' else 2)(st.selectbox('CAEC (Consumption of food between meals):', ['Sometimes', 'Frequently', 'No', 'Always']))
    smoke = (lambda x : 1 if x=='Yes' else 0)(st.selectbox('SMOKE (Do you smoke?):', ['Yes', 'No']))
    ch2o = st.number_input('CH2O (Consumption of water per day in liters):', min_value=0.1, max_value=10.0, step=0.1)
    scc = (lambda x : 1 if x=='Yes' else 0)(st.selectbox('SCC (Current physical activity level):', ['Yes','No']))
    faf = st.number_input('FAF (Frequency of physical activity per week):', min_value=0, max_value=7, step=1)
    tue = st.number_input('TUE (Time spent on exercise or activity in hours per week):', min_value=0, max_value=168, step=1)
    calc = (lambda x:1 if x=='Sometimes' else 2 if x=='No' else 0)(st.selectbox('CALC (Do you consume alcohol?):', ['Sometimes', 'No' , 'Frequently']))
    mtrans = (lambda x: 0 if x=='Automobile' else 1 if x=='Bike' else 2 if x=='Motorbike' else 3 if x=='Public_Transportation' else 4)(st.selectbox('MTRANS (Transportation mode):', ['Public_Transportation', 'Automobile', 'Walking', 'Motorbike','Bike']))
    bmi = weight/(height/100)**2
    # Collect all the encoded inputs into a list
    input_list = [[gender, age, height, weight, family_history_with_overweight, favc, fcvc, ncp, caec,
            smoke, ch2o, scc, faf, tue, calc, mtrans, bmi]]

    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()

