# Import dependencies
import pandas as pd
import numpy as np

# Load the dataset in a dataframe object and include only four features as mentioned

df=pd.read_excel('final.xlsx',header=0)

#genera cines

cines=pd.get_dummies(data=df['cine'], drop_first=True)
df=pd.concat([df, cines], axis=1)
#print(cines.info())
df.drop("cine", axis = 1, inplace=True)
df.drop("formato", axis = 1, inplace=True)
#genera sellos

sellos=pd.get_dummies(data=df['sello'], drop_first=True)
df=pd.concat([df, sellos], axis=1)
#print(cines.info())
df.drop("sello", axis = 1, inplace=True)

#genera screen

screens=pd.get_dummies(data=df['screen'], drop_first=True)
df=pd.concat([df, screens], axis=1)
df.drop("screen", axis = 1, inplace=True)
#print(df.info())
#df.drop("salas", axis = 1, inplace=True)

#print(df.info())
#genera generos

generos=pd.get_dummies(data=df['genero'], drop_first=True)
df=pd.concat([df, generos], axis=1)
df.drop("genero", axis = 1, inplace=True)

#algoritmo a utilizar, regresion lineal multiple

from sklearn.linear_model import LinearRegression




lr=LinearRegression()

#variables de entrenamiento x

x=df[["week","salas","ARECIBO","ARUBA MEGAPLEX","AUTO CINE SANTANA","BARCELONETA","BELTZ OUTLET","C3TECH","CINEMARK CURACAO","CINEMAS AT PASEO","COLE BAY (MEGAPLEX)","DORADO","E DE VEER ARUBA","FAJARDO","FINE ARTS","FINE ARTS CAFE","GUAYAMA","ISABELA","LAS AMERICAS","LAS CATALINAS","LAS PIEDRAS","LOS COLOBOS","MARKET SQUARE","METRO","MONTEHIEDRA","MOVIE CURACAO","PLAZA CAROLINA","PLAZA CAYEY","PLAZA DEL CARIBE","PLAZA DEL NORTE","PLAZA DEL SOL","PLAZA ESCORIAL","PLAZA GUAYNABO","PONCE TOWNE","RIO HONDO I","RIO HONDO II","SAN GERMAN","SAN PATRICIO","SANTA ISABEL CINEMAS","ST CROIX","ST. KITTS","TEATRO BALLAJA","TEATRO EXCELSIOR CABO ROJO","TEATRO HOLLYWOOD","TEATRO MUNICIPIO GUAYAMA","TEATRO NARANJITO","TEATRO ROOSEVELT","TEATRO SAN RAFAEL","TORTOLA","TOWN CENTER CINEMA CORP","VEGA ALTA","WESTERN PLAZA","YAUCO","FOX","IND","LIO","LOC","OTHERS","PAR","PF","PPI","SPR","UNI","UPI","WB","WDI","WF","3D","4DX","CXC","IMAX","adventure","animation","comedy","drama","horror","romcom","superheroes"]]

#variable objetivo

y=df['admission']


lr.fit(x,y)

# Save your model
#from sklearn.externals import joblib
from joblib import dump, load
dump(lr, 'model.pkl')
print("Model dumped!")

# Load the model that you just saved
lr = load('model.pkl')

# Saving the data columns from training
model_columns = list(x.columns)
dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")
print(df.info())
