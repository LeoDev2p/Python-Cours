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

#* Excepciones de sqlite3
"""
- sqlite3.IntegrityError
    - UNIQUE Constraint failed: Intentas insertar un username que ya existe o repetir la pareja (id_user, id_project) en tu tabla intermedia.
    - NOT NULL Constraint failed: Intentas crear una tarea sin ponerle un título (title).
    - FOREIGN KEY Constraint failed: Intentas asignar una tarea a un id_user que no existe en la tabla users (requiere PRAGMA foreign_keys = ON).
    - CHECK Constraint failed: Intentas insertar un usuario con un rol que no sea 'admin' o 'user' (si añadiste el CHECK que sugerimos).

- sqlite3.OperationalError
    - no such table / no such column: Escribiste mal el nombre de la tabla tasks o pediste una columna que no existe.
    - database is locked: Tienes la base de datos abierta en otro programa (como DB Browser) y Python intenta escribir al mismo tiempo.
    - unable to open database file: El archivo .db no tiene permisos de escritura o la ruta es incorrecta.
    - syntax error: Te faltó una coma , o un paréntesis ) en tu cadena de texto SQL.

- sqlite3.ProgrammingError
    - Incorrect number of bindings: Pusiste 3 signos de interrogación ? en el query, pero en los args solo pasaste 2 valores.
    - Cannot operate on a closed connection: Intentas hacer un execute() después de que el bloque with cerró la conexión.
    - Un-hashable type: Intentas pasar una lista completa como un solo parámetro en lugar de una tupla o valor simple.

- sqlite3.DatabaseError
    - File is not a database: El archivo que intentas abrir es un .txt renombrado a .db o está vacío.
    - Database disk image is malformed: El archivo se corrompió (por ejemplo, se apagó la PC mientras escribía).

- sqlite3.Error
    - Se usa en el except cuando quieres capturar cualquier error de SQLite sin importar cuál sea. Es útil para hacer un log general antes de cerrar la app.
"""