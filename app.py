from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    name='julio'
    return render_template('index.html',nombre=name)

if __name__ == "__main__":
    app.run(port=1234)