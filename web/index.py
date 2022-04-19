from flask import Flask,render_template,request,url_for,session
import sqlite3

app=Flask(__name__)

@app.route('/')

#def login():
    #return render_template('prueba.html')

def hola():
    return render_template('home.html')
    

@app.route('/adminvacantes')
def adminvacantes():
    return render_template('adminvacantes.html')

@app.route('/admincandidatos')
def admincandidatos():
    return render_template('admincandidatos.html')

@app.route('/centromensajes')
def centro():
    return render_template('centromensajes.html')

@app.route('/actividades')
def actividades():
    return render_template('actividades.html')

if __name__== '__main__':
    app.run(debug=True)