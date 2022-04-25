import sqlite3      

conn=sqlite3.connect('recursos_humanos.db')

conn.execute('CREATE TABLE IF NOT EXISTS RH(id INTEGER,nombre TEXT,email TEXT,contraseña TEXT)')
print("Tabla creada exitosamente")
conn.close()