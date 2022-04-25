import sqlite3

conn=sqlite3.connect('empleados.db')

conn.execute('CREATE TABLE IF NOT EXISTS operadores(id INTEGER,nombre TEXT,email TEXT,contraseña TEXT,kardex TEXT)')
print("Tabla creada exitosamente")
conn.close()