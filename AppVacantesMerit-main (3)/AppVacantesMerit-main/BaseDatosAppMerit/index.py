from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcrud'
mysql = MySQL(app)


app.secret_key = "mysecretkey"

@app.route('/centro')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM adminmensajes')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        id = request.form['id']
        text = request.form['text']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO adminmensajes (id, text, phone, email) VALUES (%s,%s,%s,%s)', (id, text, phone, email, ))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM adminmensajes WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editcontact.html', adminmensajes = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        text = request.form['text']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE adminmensajes
            SET  = text = %s,
                phone = %s,
                email = %s
            WHERE id = %s
        """, (text,phone,email, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM adminmensajes WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('INdex'))




def login():
    return render_template('login.html')

@app.route('/msjpostulantes')
def msjpostulantes():
    return render_template('msjpostulantes.html')

@app.route('/adminvacantes')
def adminvacantes():
    return render_template('adminvacantes.html')

@app.route('/admincandidatos')
def admincandidatos():
    return render_template('admincandidatos.html')

@app.route('/centro')
def centro():
    return render_template('index.html')

@app.route('/actividades')
def actividades():
    return render_template('actividades.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)