from flask import Flask, request, jsonify,render_template, redirect, url_for,make_response
from modelo import load_object
from flask_cors import CORS
import traceback
import json
import pandas as pd
import numpy as np
from cines import lista
import pickle

app=Flask(__name__)
CORS(app)

@app.route('/cines')
def cines():
    return jsonify(lista)

@app.route("/vista")
def vista():
    return render_template('ver.html')

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():    
    
    if lr:
       try:
          json_ = request.get_json()
          #print(json_)        
          #prediction=pd.DataFrame(json_)
          query = pd.get_dummies(pd.DataFrame(json_,index=[0]))
          #query = query.reindex(columns=model_columns, fill_value=0)
          #d =  {'id': 'CS2_056', 'cost': 2, 'name': 'Tap'}
          #df = pd.DataFrame([d], columns=d.keys(),index=[0])
          prediction = list(lr.predict(query))
          #return render_template('ver.html',prediction)
          return jsonify({'prediccion':round(prediction[0])})

       except:
          return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 1234 # If you don't provide any port the port will be set to 12345

    #lr = load("model.pkl") # Load "model.pkl"
    # cargamos cuando haga falta
    lr = load_object('modelo.pkl')
    
    print ('Model loaded')
    #model_columns = load("model_columns.pkl") # Load "model_columns.pkl"
    #print ('Model columns loaded')

    app.run(port=port, debug=True)