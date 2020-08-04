# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:46:02 2020

@author: sabab
"""
import streamlit as st
from flask import Flask, request
import  pandas as pd
import numpy as np
import pickle
import flasgger 
from flasgger import Swagger
from PIL import Image

app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
scaler_in = open('scaler.pkl', 'rb')
scaler = pickle.load(scaler_in)


@app.route('/')
def welcome():
    return "welcome all"

@app.route('/predict')
def predict_heart_disease(age, cp, rbp, sc, max_hr, angina, st_rest, peak_st, mv, thal):
  
    """
    Predict Chances of Heart Disease.
    
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Age
        in: query
        type: number
        required: true
      - name: Chest Pain
        in: query
        type: number
        required: true
      - name: Resting Blood Pressure
        in: query
        type: number
        required: true
      - name: Serum Cholestrol
        in: query
        type: number
        required: true
      - name: Max Heart Rate
        in: query
        type: number
        required: true
      - name: Angima
        in: query
        type: number
        required: true
      - name: ST Rest
        in: query
        type: number
        required: true
      - name: Peak ST
        in: query
        type: number
        required: true
      - name: Major vessels
        in: query
        type: number
        required: true
      - name: Thal
        in: query
        type: number
        required: true
        
    responses:
        200:
            description: The output values

    """
    
    model_input = scaler.transform([[age, cp, rbp, sc, max_hr, angina, st_rest, peak_st, mv, thal]])
    
    prediction = classifier.predict(model_input)
    
    return "The predicted value is " + str(prediction)


@app.route('/predict_file', methods = ["POST"])
def predict_heart_disease_file():
    """
    Predict Chances of Heart Disease.
    
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    
    responses:
        200:
            description: The output values
        
    """
    df_test = pd.read_csv(request.files.get("file"))
    
    prediction = classifier.predict(scaler.transform(df_test))

    return str(list(prediction))


    





def main():
  
    html_temp="""
    <div style ="background-color: #E94F1C; padding:10px">
    <h2 style="color:white; text-align:center;">Heart Disease Predictor</h2>
    </div>
    """
    # html_temp = """
    # <div style="background-color:tomato;padding:10px">
    # <h2 style="color:white;text-align:center;">Heart Disease Predictor</h2>
    # </div>
    # """
    st.markdown(html_temp, unsafe_allow_html=True)
    image = Image.open('bc.jpg')
    st.image(image,use_column_width=True)
    st.subheader("Please fill up the following information:")
    age = st.text_input('Age', type='default')
    cp_text = st.selectbox('Chest pain type',('Typical angina (1)', 'Atypical angina (2)', 'Non-anginal pain (3)', 'Asymtoptic (4)'))
    
    if cp_text == "Typical angina (1)":
        cp=1
    elif cp_text == "Atypical angina (2)":
        cp=2
    elif cp_text == "Non-anginal pain (3)":
        cp=3
    else:
        cp=4
        
    rbp = st.text_input('Resting blood pressure in mmHg', type='default')
    
    sc = st.text_input('Serum cholestrol in mg/dl', type='default')
    
    max_hr = st.text_input('Max heart rate', type='default')
    
    angina_text = st.selectbox('Exercised induced angina', ('Yes (1)', 'No (0)'))
    if angina_text == "Yes (1)":
        angina = 1
    else:
        angina = 0
    
    st_rest = st.text_input('ST depression induced by exercise relative to rest', type='default')
    
    peak_st_text = st.selectbox('Peak exercise ST segment', ('Upsloping (1)', 'Flat (2)', 'Downsloping (3)'))
    if peak_st_text == "Upsloping (1)":
        peak_st = 1
    elif peak_st_text == "Flat (2)":
        peak_st = 2
    else:
        peak_st = 3
    
    mv = st.radio('Number of major vessels (0–3) colored by flourosopy', (0,1,2,3))
    
    thal_text = st.selectbox('Thalassemia', ('Normal (3)', 'Fixed defect (6)', 'Reversible defect (7)'))
    if thal_text == "Normal (3)":
        thal = 3
    elif thal_text == "Fixed defect (6)":
        thal = 6
    else:
        thal = 7 
    result=""
    
    if st.button("Predict"):
        result = predict_heart_disease(age, cp, rbp, sc, max_hr, angina, st_rest, peak_st, mv, thal)
        if int(result[-3]) == 1:
            st.error("Yoh have higher chances of having a heart disease.".format(result))
        else:
            st.success("Yoh have lower chances of having a heart disease.".format(result))

    if st.button("About"):
        st.text("Copyright: Shahed Anzarus Sabab")
        
        
    
if __name__ == '__main__':
    main()