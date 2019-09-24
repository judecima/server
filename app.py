from flask import Flask,request,render_template

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
    
    
    
    return render_template('pantalla.html',cines=cine)


if __name__ == "__main__":
    app.run(debug=True,port=1234)
