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
def predict_heart_disease(age, cp, rbp, sc, max_hr, angima, st_rest, peak_st, mv, thal):
  
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
    
    model_input = scaler.transform([[age, cp, rbp, sc, max_hr, angima, st_rest, peak_st, mv, thal]])
    
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
    st.title("Predict Heart Disease")
    html_temp="""
    <div style ="background-color: tomato; padding:10px">
    <h2 style="color:white; text-align:center;>Streamlit Heart Disease Predictor App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input('Age', 'Type Here')
    cp = st.text_input('Chest Pain', 'Type Here')
    rbp = st.text_input('Resting Blood Pressure', 'Type Here')
    sc = st.text_input('Serum Cholestrol', 'Type Here')
    max_hr = st.text_input('Max Heart Rate', 'Type Here')
    angima = st.text_input('Angima', 'Type Here')
    st_rest = st.text_input('ST Rest', 'Type Here')
    peak_st = st.text_input('Peak ST', 'Type Here')
    mv = st.text_input('Major vessels', 'Type Here')
    thal = st.text_input('Thal', 'Type Here')
    
    result=""
    
    if st.button("Predict"):
        result = predict_heart_disease(age, cp, rbp, sc, max_hr, angima, st_rest, peak_st, mv, thal)
        if int(result[-3]) == 1:
            st.error("Yoh have higher chances of having a heart disease.".format(result))
        else:
            st.success("Yoh have lower chances of having a heart disease.".format(result))

    if st.button("About"):
        st.text("Copyright: Shahed Anzarus Sabab")
        
        
    
if __name__ == '__main__':
    main()