import sqlite3

#* OJO: con with el commit () y close es automatico

"""
connect () -> Establece una conexión con la base de datos SQLite.
cursor ()  -> Crea un cursor para ejecutar comandos SQL.

execute ()  -> Ejecuta un comando SQL único.
executemany ()  -> Ejecuta un comando SQL con múltiples conjuntos de parámetros.

close ()  -> Cierra la conexión a la base de datos.
"""

# Conectamos con la base de datos (o la creamos si no existe)
with sqlite3.connect ("example.db") as conn:
    cursor = conn.cursor ()  # Creamos un cursor para ejecutar comandos SQL

    # execute () -> para ejecutar SQL
    cursor.execute ("""
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT
,           title TEXT NOT NULL,
            director TEXT NOT NULL,
            year INTEGER NOT NULL,
            rating REAL
            )
    """)

#* Insertando datos en la tabla ---------------------------

"""
execute ()  -> Ejecuta un comando SQL único.
executemany ()  -> Ejecuta un comando SQL con múltiples conjuntos de parámetros.
"""

with sqlite3.connect ("example.db") as conn:
    cursor = conn.cursor ()

    # en INSERT usamos ? como marcadores de posición para los valores y Evitan errores y SQL injection
    cursor.execute ("""
        INSERT INTO movies (title, director, year, rating)
        VALUES (?, ?, ?, ?)
    """, ("Inception", "Christopher Nolan", 2010, 8.8)
    )

    movies = [
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Interstellar", "Christopher Nolan", 2014, 8.6),
    ("The Dark Knight", "Christopher Nolan", 2008, 9.0)]

    cursor.executemany(
        "INSERT INTO movies (title, director, year, rating) VALUES (?, ?, ?, ?)",
        movies
    )

#* Leer datos de la tabla -------------------------------

"""
fetchone ()  -> Recupera la primera fila de un conjunto de resultados de una consulta.
fetchall ()  -> Recupera todas las filas de un conjunto de resultados de una consulta.
fetchmany (n)  -> Recupera un número específico de filas (n) de un conjunto de resultados de una consulta.
"""

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor ()

    cursor.execute ("""
        SELECT * FROM movies
    """)

    data = cursor.fetchmany (4)

    print (data)

#* Actualizar datos en la tabla ---------------------------

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor ()

    cursor.execute ("""
        UPDATE movies
        SET rating = ?
        WHERE title = ?
    """, (9.1, "Inception")
    )

#* Eliminar datos de la tabla -----------------------------
with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor ()

    cursor.execute ("""
        DELETE FROM movies
        WHERE title = ?
    """, ("Interstellar",)
    )