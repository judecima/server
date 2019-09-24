from flask import Flask, request, jsonify,render_template
from joblib import dump, load
import traceback
import pandas as pd
import numpy as np


app=Flask(__name__)

@app.route('/')
def inicio():
    generos = ['action','adventure','animation','comedy','drama','horror','romcom','superheroes']
    cines= ['AGUADILLA','ARECIBO', 'ARUBA MEGAPLEX', 'BARCELONETA', 'BELTZ OUTLET', 'COLE BAY (MEGAPLEX)', 'DORADO','FAJARDO', 'FINE ARTS', 'FINE ARTS CAFE', 'GUAYAMA','ISABELA', 'LAS AMERICAS', 'LAS CATALINAS', 'LAS PIEDRAS', 'LOS COLOBOS', 'MARKET SQUARE', 'METRO', 'MONTEHIEDRA', 'PLAZA CAROLINA', 'PLAZA CAYEY', 'PLAZA DEL CARIBE', 'PLAZA DEL NORTE', 'PLAZA DEL SOL', 'PLAZA ESCORIAL', 'PLAZA GUAYNABO', 'PONCE TOWNE', 'RIO HONDO I', 'RIO HONDO II', 'SAN GERMAN', 'SAN PATRICIO', 'SANTA ISABEL CINEMAS', 'ST CROIX', 'ST. KITTS', 'VEGA ALTA', 'WESTERN PLAZA', 'YAUCO']
    zonas=['INTERIOR','ISLAS VIRGENES', 'METROPOLITANA']
    circuitos=['CARIBBEAN CINEMAS','INDEPENDENT','EL CINE']
    sellos=['BVI','FOX', 'IND', 'LIO', 'LOC','OTHERS' ,'PAR', 'PF', 'PPI', 'SPR', 'UNI', 'UPI', 'WB', 'WDI', 'WF']
    sem=range(1,53)
    semanas=list(sem)
    return render_template('index.html',generos=generos,cines=cines,circuitos=circuitos,zonas=zonas,sellos=sellos,semanas=semanas)

@app.route('/ver',methods=['POST'])
def ver():
    cine=request.form
    cine1=request.form.values()
    ver="locura"
    
    
    return render_template('index.html',ver=ver)


@app.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_,index=[0]))
            #query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    lr = load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)