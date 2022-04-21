from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)


app.secret_key = "mysecretkey"

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        vacante = request.form['vacante']
        descripcion = request.form['descripcion']
        originario = request.form['originario']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (vacante, descripcion,originario) VALUES (%s,%s,%s)',
        (vacante,descripcion,originario))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        vacante = request.form['vacante'] 
        descripcion = request.form['descripcion']
        originario = request.form['originario']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET vacante = %s,
                descripcion = %s,
                originario = %s
            WHERE id = %s
        """, (vacante,descripcion,originario, id))
        flash('Vacante Actualizada Correctamente')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Vacante Removida Correctamente')
    return redirect(url_for('Index'))

@app.route('/añadir/<id>', methods = ['POST', 'GET'])
def añadir_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('añadir.html', contact = data[0])



if __name__ == "__main__":
    app.run(port=5000, debug=True)
