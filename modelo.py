# Import dependencies
import pandas as pd
import numpy as np

# Load the dataset in a dataframe object and include only four features as mentioned
url = pd.read_excel('base.xlsx',header=0)
df = pd.read_csv(url)


#generar dummies de las variables categoricas

#generar variables generos
generos=pd.get_dummies(data=df['genero'], drop_first=True)
df=pd.concat([df, generos], axis=1)
df.drop("genero", axis = 1, inplace=True)

#genera variables circuitos
circuitos=pd.get_dummies(data=df['circuitos'], drop_first=True)
df=pd.concat([df, circuitos], axis=1)
df.drop("circuitos", axis = 1, inplace=True)

#genera cines
cines=pd.get_dummies(data=df['cine'], drop_first=True)
df=pd.concat([df, cines], axis=1)
df.drop("cine", axis = 1, inplace=True)
#genera cines
zonas=pd.get_dummies(data=df['zona'], drop_first=True)
df=pd.concat([df, zonas], axis=1)
df.drop("zona", axis = 1, inplace=True)
#genera sellos
sellos=pd.get_dummies(data=df['sello'], drop_first=True)
df=pd.concat([df, sellos], axis=1)
df.drop("sello", axis = 1, inplace=True)


# Logistic Regression classifier
from sklearn.linear_model import LinearRegression

lr=LinearRegression()
x=df[['mes','ano','week','adventure','animation','comedy','drama','horror','romcom','superheroes','ARECIBO','ARUBA MEGAPLEX','BARCELONETA','BELTZ OUTLET','COLE BAY (MEGAPLEX)','DORADO','FAJARDO','FINE ARTS','FINE ARTS CAFE','GUAYAMA','ISABELA','LAS AMERICAS','LAS CATALINAS','LAS PIEDRAS','LOS COLOBOS','MARKET SQUARE','METRO','MONTEHIEDRA','PLAZA CAROLINA','PLAZA CAYEY','PLAZA DEL CARIBE','PLAZA DEL NORTE','PLAZA DEL SOL','PLAZA ESCORIAL','PLAZA GUAYNABO','PONCE TOWNE','RIO HONDO I','RIO HONDO II','SAN GERMAN','SAN PATRICIO','SANTA ISABEL CINEMAS','ST CROIX','ST. KITTS','VEGA ALTA','WESTERN PLAZA','YAUCO','ISLAS VIRGENES','METROPOLITANA','FOX','IND','LIO','LOC','PAR','PF','PPI','SPR','UNI','UPI','WB','WDI','WF']]
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