
# --------------------------------------------------------------------------------------
#  ------------------------------- SQLite 3  NIVEL BASICO ----------------------------

# Tipos de datos

"""
OJO: SQLIte no tiene tipo booleano se repsentan con 0 y 1

NULL     : Valor Nulo
INTEGER  : Entero (positivo / negativo)
REAL     : Numero Decimal (float)
TEXT     : Texto
BLOB     : Datos binarios (imágenes, pdf, audio, etc.)
"""

# Operadores artiméticos

"""
+    : Suma
-    : Resta
*    : Multiplicación
/    : División
%    : Módulo
**   : Exponente
"""

# Operadores de comparación

"""
=           : Igual que
!= o <>     : Distinto que
>           : Mayor que
<           : Menor que
>=          : Mayor o igual que
<=          : Menor o igual que
"""

# Operadores lógicos

"""
AND         : Y
OR          : O
NOT         : NO
"""


#  -----------------------------------------------------

# CREATE TABLE -> En toda tabla debe de haber su PRIMARY KEY

"""
CREATE TABLE nombre_tabla (
    columna1 TIPO_DATO,
    columna2 TIPO_DATO,
    columna3 TIPO_DATO
)
"""
# PRIMARY KEY -> Clave primaria (Identificador único)
# AUTOINCREMENT -> Incrementa automáticamente el valor de la clave primaria
# NOT NULL -> No permite valores nulos (columnas nulos)
# UNIQUE -> No permite valores duplicados en la columna
# DEFAULT -> Valor por defecto si no se especifica ningún valor
# CHECK (expresion math) -> Restringe los valores que se pueden insertar en una columna

# Ejercicios

# Crear una tabla
"""
CREATE TABLE Nombre_tabla (
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"Nombres" TEXT,
	"Edad" INTEGER CHECK (Edad > 0),
	"Email" TEXT UNIQUE NOT NULL,
	"Password" TEXT NOT NULL,
	"Active" INTEGER DEFAULT 1
);

"""

# INsertar datos en la tabla

"""
INSERT INTO Nombre_tabla
VALUES (
    NULL,
	"Isaias Cesar Quintana Errazabal",
	23,
	"cesar@gmail.com",
	"Cesar123",
	0
);

# envias a columnas especificas y/o por lote (que no tenge NOT NULL)

INSERT INTO Nombre_tabla ("Edad", "Email", "Password")
VALUES (23, "cesar@gmail.com", "Cesar123"),
        (22, "juan@gmail.com", "Juan123");
        (25, "maria@gmail.com", "Maria123");
"""

# Leer datos de la tabla

"""
SELECT * FROM Nombre_tabla   # Leer todos los datos de la tabla
SELECT columna1, columna2 FROM tabla;  # Leer datos específicos de la tabla

SELECT * FROM Nombre_tabla WHERE columna > 18 AND active = 1;  # Filtrar datos con condiciones (AND : indica ambas de cumplen)

SELECT * FROM Nombre_tabla ORDER BY columna DESC;  # Ordenar los datos por edad de forma descendente
"""

# Actualizar datos en la tabla

"""
UPDATE Nombre_tabla
SET columna1 = valor1, columna2 = valor2, ....
WHERE condicion;
"""

# Eliminar datos en la tabla

"""
DELETE FROM tabla
WHERE condicion;
"""

# DROP TABLE -> eiminar tabla
"""
DROP TABLE nombre_tabla;
DROP TABLE IF EXISTS nombre_tabla;
"""

# ALTER TABLE -> Modificar tabla existente agregando una nueva columna uno por uno
"""
ALTER TABLE nombre_tabla
ADD COLUMN nombre_columna TIPO;

OJO: NO puedes agregar una columna NOT NULL sin valor por defecto

------------------ Renombrar columna ------------------
ALTER TABLE nombre_tabla
RENAME COLUMN length_minutes TO duration;

------------------ Renombrar tabla ------------------
ALTER TABLE nombre_tabla
RENAME TO films;
"""


#  ***************** Operadores especiales **************

# SINTAXIS DE CADA PALABRA RESERVADA ->->->->->->_>_>->-

#  	WHERE   --> Filtrar resultados con condiciones
"""
SELECT * FROM tabla
WHERE condicion;
"""

# AND, OR, NOT   --> Combinación de condiciones
"""
WHERE condicion1 AND condicion2
WHERE condicion1 OR condicion2
WHERE NOT condicion
"""

# ORDER BY    ASC / DESC  --> Ordenar los resultados
"""
SELECT * FROM tabla
ORDER BY columna ASC/DESC;
"""

# LIMIT --> Limitar el número de resultados devueltos
"""
SELECT * FROM tabla
LIMIT numero;
"""

# OFFSET  --> Omitir un número específico de resultados antes de comenzar a devolver filas
"""
SELECT * FROM tabla
LIMIT numero OFFSET numero;

Ojito con OFFSET:  siempre va despues de LIMIT Y acompañado de un ORDER BY
"""

# DISTINCT  --> Eliminar duplicados en los resultados
"""
SELECT DISTINCT columna
FROM tabla;
"""

# -----------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
# -------------------------------- SQLite 3  NIVEL INTERMEDIO ----------------------------

# FILTROS AVANZADOS SINTAXIS Y CONCEPTOS

# BETWEEN --> Filtrar valores entre un rango específico
"""
WHERE columna BETWEEN valor1 AND valor2
"""

# IN  --> Filtrar valores dentro de una lista específica
"""
WHERE columna IN (valor1, valor2, valor3, ...)
"""

# LIKE --> Filtrar valores que coincidan con un patrón específico (no CaseSensitive)
"""
WHERE columna LIKE 'patrón';

Comodines importantes

% → cualquier cantidad de caracteres (incluyendo ninguno)
_ → un solo carácter
"""

# GLOB --> Filtrar valores que coincidan con un patrón específico (CaseSensitive)
"""
WHERE columna GLOB 'patrón';
"""

# IS NULL  --> Filtrar campos con valores nulos (vacia)
""""
WHERE columna IS NULL;
WHERE columna IS NOT NULL;
"""

# * Funciones de agregación *
# ROUND() --> Redondear valores numéricos
"""
SELECT ROUND (COUNT(columna)) FROM tabla;
"""
# GROUP_CONCAT() --> Concatenar valores de una columna en una sola cadena separada por comas
"""
SELECT GROUP_CONCAT(columna) FROM tabla;
"""

# COUNT() --> Contar el número de filas que cumplen una condición específica
"""
SELECT COUNT(columna) FROM tabla;
SELECT COUNT(*) FROM tabla;
"""

# SUM() --> Sumar los valores de una columna específica
"""
SELECT SUM(columna) FROM tabla;
"""

# AVG() --> Calcular el promedio de los valores de una columna específica
"""
SELECT AVG(columna) FROM tabla;
"""
# MAX() / MIN () --> Obtener el valor máximo y minimo de una columna específica
"""
SELECT MIN(columna) FROM tabla;
SELECT MAX(columna) FROM tabla;
"""

# GROUP BY --> Agrupar los resultados por una o más columnas
"""
SELECT columna, FUNCION(columna)
FROM tabla
GROUP BY columna;

OJO: TODA columna que aparece en SELECT y NO está en una función (COUNT, SUM, etc.)
DEBE estar en GROUP BY
"""

# HAVING --> Filtrar los resultados agrupados por una o más condiciones
"""
SELECT columna, COUNT(*)
FROM tabla
GROUP BY columna
HAVING COUNT(*) > 2;

OJO: WHERE filtra filas  |  HAVING filtra grupos
"""

# AS --> Renombrar columnas o tablas en los resultados durante la consulta
"""
FROM movies AS m  -> Tabala

SELECT columna AS alias, sum(columna) AS total_sum  --> Columnas
FROM tabla;

OJO: lo recomnendable usar alias de columnas en el ORDER BY
"""

# Orden  ejecución de las cláusulas SQL
"""
1️⃣ FROM
2️⃣ WHERE
3️⃣ GROUP BY
4️⃣ HAVING
5️⃣ SELECT ← aquí recién se crean los alias
6️⃣ ORDER BY
"""

# * Relaciones de tablas *
# * 1 a muchos (1:N)   .> Foreign Key
# *-  director -> muchas peliculas |  una pelicula  -> un director

"""
--> La tabla hija usa la misma PK que la tabla padre como FK y PK.

movies (
  id INTEGER PRIMARY KEY,
  title TEXT,
  year INT,
  rating REAL
)

movie_details (
  movie_id INTEGER PRIMARY KEY,  
  duration INT,
  budget REAL,
  language TEXT,
  FOREIGN KEY (movie_id) REFERENCES movies(id)
)

"""

# * Muchos a muchos (N:M)
# *- pelicula -> muchos actores  |  un actor -> actua en muchas peliculas <-

"""
CREATE TABLE actors (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE movies_actors (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	movie_id INTEGER,
	actor_id INTEGER

    FOREIGN KEY (movie_id) REFERENCES movies (id)
    FOREIGN KEY (actor_id) REFERENCES actors (id)
);

CREATE TABLE movies (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	year INTEGER,
	director_id INTEGER,
    
);
"""

# * 1 a 1 (1:1)
# *- estudiante -> tiene un DNI  |  DNI ->  pertence estudiante

"""
CREATE TABLE directors (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE movies (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	year INTEGER,
	director_id INTEGER,
    
	FOREIGN KEY (director_id) REFERENCES directors (id) -><-
);
"""

# INNER JOIN --> Combinar filas de dos o más tablas usando una columna en común.
"""
SELECT columna_tabla1, columna_tabla2, ....
FROM tabla1
INNER JOIN tabla2
ON tabla1.columna = tabla2.columna;
"""
# OJO: orden ejecucion SQL con INNER JOIN
"""
SELECT ...
FROM tabla1
JOIN tabla2 ON ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...
"""

# LEFT JOIN --> “Tráeme TODO de la tabla izquierda + los que no coinciden”
"""
SELECT columnas
FROM tabla_izquierda
LEFT JOIN tabla_derecha
ON condicion;
"""

# Subconsultas --> Consulta dentro de otra consulta

#* Subconsulta en un WHERE	
"""
--> **** Comparar con un valor calculado (100% pre devulve una sola columna y una sola fila)

SELECT columnas
FROM tabla
WHERE columna operador (SELECT columna FROM tabla);
"""

#* Subconsulta en un IN
"""
--> **** Comparar con una lista de valores (una columna)

SELECT columnas
FROM tabla
WHERE columna IN (SELECT columna FROM tabla);
"""

#* EXISTS --> Verificar la existencia de al menos una filas que cumplan una condición específica
"""
SELECT columnas
FROM tabla_externa
WHERE EXISTS (
    SELECT 1
    FROM tabla_interna
    WHERE condición_relacionada
);
"""

#* ALL --> Comparar si todos los devuelto por una subconsulta cumplen
#* ANY --> Comparar si al menos un valor devuelto por una subconsulta cumple
"""
SELECT columnas
FROM tabla_externa
WHERE columna comparacion ALL/ANY (subconsulta);
"""

#* Subconsulta en un SELECT
"""
--> **** Debe devolver una sola columna y sola fila normalmente

SELECT columna,
       (SELECT algo FROM tabla) AS nombre_columna
FROM tabla;
"""

#* Subconsulta en un FROM
"""
--> **** Crea una tabla temporal con la misma cantidad de columnas del SELECT normal

SELECT columnas
FROM (SELECT ...) AS alias
WHERE condición;
"""

#* Subconsulta correlacionada 
"""
--> ****  Comparar cada fila con su propio grupo

SELECT d.name, m.title, m.rating
FROM movies m
INNER JOIN directors d ON m.director_id = d.id
WHERE m.rating = (
    SELECT MAX(m2.rating)
    FROM movies m2
    WHERE m2.director_id = m.director_id
);
"""
