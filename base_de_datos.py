import sqlite3

conexion = sqlite3.connect("mis_tareas.db")
cursor = conexion.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS tareas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   descripcion TEXT NOT NULL,
                   prioridad TEXT NOT NULL
               )
               ''')
descripcion = "Aprender sql con mi mentor"
prioridad = "Alta"

cursor.execute('''INSERT INTO tareas (descripcion, prioridad) VALUES (?, ?)''', (descripcion, prioridad))

conexion.commit()
print("¡Tarea guardada en la base de datos!")
conexion.close()