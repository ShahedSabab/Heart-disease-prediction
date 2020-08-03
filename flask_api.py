# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 04:27:26 2020

@author: sabab
"""

from flask import Flask, request
import  pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


@app.route('/predict')
def predict_heart_disease():
    sc = request.args.get('Serum Cholestrol')
    peak_st = request.args.get('Peak ST')
    rbp = request.args.get('Resting Blood Pressure')
    age = request.args.get('Age')
    st_rest = request.args.get('ST Rest')
    max_hr = request.args.get('Max Heart Rate')
    angima = request.args.get('Angima')
    cp = request.args.get('Chest Pain')
    mv = request.args.get('Major vessels')
    thal = request.args.get('Thal')
    
    prediction = classifier.predict([[sc, peak_st, rbp, age, st_rest, max_hr, angima, cp, mv, thal]])
    return "The predicted values is " + str(prediction)