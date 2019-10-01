from flask import Flask, request, jsonify,render_template, redirect, url_for,make_response
from joblib import dump, load
from flask_cors import CORS
import traceback
import json
import pandas as pd
import numpy as np
from cines import lista

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
    #generos = ['action','adventure','animation','comedy','drama','horror','romcom','superheroes']
    #cines= ['AGUADILLA','ARECIBO', 'ARUBA MEGAPLEX', 'BARCELONETA', 'BELTZ OUTLET', 'COLE BAY (MEGAPLEX)', 'DORADO','FAJARDO', 'FINE ARTS', 'FINE ARTS CAFE', 'GUAYAMA','ISABELA', 'LAS AMERICAS', 'LAS CATALINAS', 'LAS PIEDRAS', 'LOS COLOBOS', 'MARKET SQUARE', 'METRO', 'MONTEHIEDRA', 'PLAZA CAROLINA', 'PLAZA CAYEY', 'PLAZA DEL CARIBE', 'PLAZA DEL NORTE', 'PLAZA DEL SOL', 'PLAZA ESCORIAL', 'PLAZA GUAYNABO', 'PONCE TOWNE', 'RIO HONDO I', 'RIO HONDO II', 'SAN GERMAN', 'SAN PATRICIO', 'SANTA ISABEL CINEMAS', 'ST CROIX', 'ST. KITTS', 'VEGA ALTA', 'WESTERN PLAZA', 'YAUCO']
    #zonas=['INTERIOR','ISLAS VIRGENES', 'METROPOLITANA']
    #circuitos=['CARIBBEAN CINEMAS','INDEPENDENT','EL CINE']
    #sellos=['BVI','FOX', 'IND', 'LIO', 'LOC','OTHERS' ,'PAR', 'PF', 'PPI', 'SPR', 'UNI', 'UPI', 'WB', 'WDI', 'WF']
    #sem=range(1,53)
    #semanas=list(sem)
    return render_template('index.html')#,generos=generos,cines=cines,circuitos=circuitos,zonas=zonas,sellos=sellos,semanas=semanas)
"""
@app.route('/ver',methods=['POST'])
def ver():
    #generos = ['action','adventure','animation','comedy','drama','horror','romcom','superheroes']
    #cines= ['AGUADILLA','ARECIBO','ARUBA MEGAPLEX','AUTO CINE SANTANA','BARCELONETA','BELTZ OUTLET','C3TECH','CINEMARK CURACAO','CINEMAS AT PASEO','COLE BAY (MEGAPLEX)','DORADO','E DE VEER ARUBA','FAJARDO','FINE ARTS','FINE ARTS CAFE','GUAYAMA','ISABELA','LAS AMERICAS','LAS CATALINAS','LAS PIEDRAS','LOS COLOBOS','MARKET SQUARE','METRO','MONTEHIEDRA','MOVIE CURACAO','PLAZA CAROLINA','PLAZA CAYEY','PLAZA DEL CARIBE','PLAZA DEL NORTE','PLAZA DEL SOL','PLAZA ESCORIAL','PLAZA GUAYNABO','PONCE TOWNE','RIO HONDO I','RIO HONDO II','SAN GERMAN','SAN PATRICIO','SANTA ISABEL CINEMAS','ST CROIX','ST. KITTS','TEATRO BALLAJA','TEATRO EXCELSIOR CABO ROJO','TEATRO HOLLYWOOD','TEATRO MUNICIPIO GUAYAMA','TEATRO NARANJITO','TEATRO ROOSEVELT','TEATRO SAN RAFAEL','TORTOLA','TOWN CENTER CINEMA CORP','VEGA ALTA','WESTERN PLAZA','YAUCO']
    #zonas=['INTERIOR','ISLAS VIRGENES', 'METROPOLITANA']
    #circuitos=['CARIBBEAN CINEMAS','INDEPENDENT','EL CINE']
    #sellos=['BVI','FOX', 'IND', 'LIO', 'LOC','OTHERS' ,'PAR', 'PF', 'PPI', 'SPR', 'UNI', 'UPI', 'WB', 'WDI', 'WF']
  
    cine=request.form.get("cine")
    sello=request.form.get("productora")
    semana=int(request.form.get("semana"))
    genero=request.form.get("genero")
    salas=int(request.form.get("sala"))
    pantallas=request.form.get("pantalla")

    valores={"week":0,"salas":0,"ARECIBO":0,"ARUBA MEGAPLEX":0,"AUTO CINE SANTANA":0,"BARCELONETA":0,"BELTZ OUTLET":0,"C3TECH":0,"CINEMARK CURACAO":0,"CINEMAS AT PASEO":0,"COLE BAY (MEGAPLEX)":0,"DORADO":0,"E DE VEER ARUBA":0,"FAJARDO":0,"FINE ARTS":0,"FINE ARTS CAFE":0,"GUAYAMA":0,"ISABELA":0,"LAS AMERICAS":0,"LAS CATALINAS":0,"LAS PIEDRAS":0,"LOS COLOBOS":0,"MARKET SQUARE":0,"METRO":0,"MONTEHIEDRA":0,"MOVIE CURACAO":0,"PLAZA CAROLINA":0,"PLAZA CAYEY":0,"PLAZA DEL CARIBE":0,"PLAZA DEL NORTE":0,"PLAZA DEL SOL":0,"PLAZA ESCORIAL":0,"PLAZA GUAYNABO":0,"PONCE TOWNE":0,"RIO HONDO I":0,"RIO HONDO II":0,"SAN GERMAN":0,"SAN PATRICIO":0,"SANTA ISABEL CINEMAS":0,"ST CROIX":0,"ST. KITTS":0,"TEATRO BALLAJA":0,"TEATRO EXCELSIOR CABO ROJO":0,"TEATRO HOLLYWOOD":0,"TEATRO MUNICIPIO GUAYAMA":0,"TEATRO NARANJITO":0,"TEATRO ROOSEVELT":0,"TEATRO SAN RAFAEL":0,"TORTOLA":0,"TOWN CENTER CINEMA CORP":0,"VEGA ALTA":0,"WESTERN PLAZA":0,"YAUCO":0,"FOX":0,"IND":0,"LIO":0,"LOC":0,"OTHERS":0,"PAR":0,"PF":0,"PPI":0,"SPR":0,"UNI":0,"UPI":0,"WB":0,"WDI":0,"WF":0,"3D":0,"4DX":0,"CXC":0,"IMAX":0,"adventure":0,"animation":0,"comedy":0,"drama":0,"horror":0,"romcom":0,"superheroes":0}
    #valores={"week":1,"adventure":1,"animation":0,"comedy":0,"drama":0,"horror":0,"romcom":0,"superheroes":0,"ARECIBO":1,"ARUBA MEGAPLEX":0,"BARCELONETA":0,"BELTZ OUTLET":0,"COLE BAY (MEGAPLEX)":0,"DORADO":0,"FAJARDO":0,"FINE ARTS":0,"FINE ARTS CAFE":0,"GUAYAMA":0,"ISABELA":0,"LAS AMERICAS":0,"LAS CATALINAS":0,"LAS PIEDRAS":0,"LOS COLOBOS":0,"MARKET SQUARE":0,"METRO":0,"MONTEHIEDRA":0,"PLAZA CAROLINA":0,"PLAZA CAYEY":0,"PLAZA DEL CARIBE":0,"PLAZA DEL NORTE":0,"PLAZA DEL SOL":0,"PLAZA ESCORIAL":0,"PLAZA GUAYNABO":0,"PONCE TOWNE":0,"RIO HONDO I":0,"RIO HONDO II":0,"SAN GERMAN":0,"SAN PATRICIO":0,"SANTA ISABEL CINEMAS":0,"ST CROIX":0,"ST. KITTS":0,"VEGA ALTA":0,"WESTERN PLAZA":0,"YAUCO":0,"ISLAS VIRGENES":1,"METROPOLITANA":0,"FOX":1,"IND":0,"LIO":0,"LOC":0,"PAR":0,"PF":0,"PPI":0,"SPR":0,"UNI":0,"UPI":0,"WB":0,"WDI":0,"WF":0}
    #print((valores))
    if (cine != 'AGUADILLA'):
        valores[cine]=1
    if (sello != 'BVI'):
        valores[sello]=1
    valores["week"]=semana
    if(genero != 'action'):
        valores[genero]=1
    valores["salas"]=salas
    if(pantallas != '2D'):
        valores[pantallas]=1
    #print((valores))
    print(cine)
    print(sello)
    print(semana)
    print(genero)
    print(salas)
    print(pantallas)
    print((valores))
    #valores=json.dumps(valores)
    #return jsonify(valores)
    #print((valores))
    #valores=json.dumps(valores)  
    
    
    if lr:
        try:
            
            
            query = query = pd.get_dummies(pd.DataFrame(valores,index=[0]))
            print(query.info())
            #query = query.reindex(columns=model_columns, fill_value=0)
            #d =  {'id': 'CS2_056', 'cost': 2, 'name': 'Tap'}
            #df = pd.DataFrame([d], columns=d.keys(),index=[0])
            #print(query.info())
            prediction = list(lr.predict(query))
            #print(prediction)
            #print(prediction)
            #return render_template('ver.html',prediction)
            res = make_response(jsonify({'prediction': round(prediction[0])}), 200)
            return res
            #return render_template('ver.html',valor=prediction)
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
    
    
    
    
"""

@app.route('/predict', methods=['POST'])
def predict():

  
    
    
    # if lr:
        # try:
    json_ = request.get_json()
    #print(json_)
    query = pd.get_dummies(pd.DataFrame(json_,index=[0]))
    
    prediction = list(lr.predict(query))
    
    res1={'prediction': str(prediction)}
    res1={'hola':12}
    res=make_response(jsonify(res1),200)
    return res    

    """        
            query = pd.get_dummies(pd.DataFrame(json_,index=[0]))
            #query = query.reindex(columns=model_columns, fill_value=0)
            #d =  {'id': 'CS2_056', 'cost': 2, 'name': 'Tap'}
            #df = pd.DataFrame([d], columns=d.keys(),index=[0])

            prediction = list(lr.predict(query))
            #return render_template('ver.html',prediction)
            return jsonify({'prediction': (prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
"""
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 1234 # If you don't provide any port the port will be set to 12345

    lr = load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)