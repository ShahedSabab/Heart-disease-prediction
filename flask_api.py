# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 04:27:26 2020

@author: sabab
"""

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
def predict_heart_disease():
  
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
    age = request.args.get('Age')
    cp = request.args.get('Chest Pain')
    rbp = request.args.get('Resting Blood Pressure')
    sc = request.args.get('Serum Cholestrol')
    max_hr = request.args.get('Max Heart Rate')
    angima = request.args.get('Angima')
    st_rest = request.args.get('ST Rest')
    peak_st = request.args.get('Peak ST')
    mv = request.args.get('Major vessels')
    thal = request.args.get('Thal')
    
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
    prediction = classifier.predict(df_test)
    return str(list(prediction))



if __name__ == '__main__':
    app.run()