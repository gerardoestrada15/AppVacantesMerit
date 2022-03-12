from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def hola():
    return render_template('home.html')
    

@app.route('/about')
def about():
    return render_template('about.html')

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