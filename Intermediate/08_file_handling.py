
#  ------------------------- Archivos TXT -------------------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ruta_txt = BASE_DIR / "Intermediate" / "my_file.txt"

"""
Modo	Significado

"r"  	leer
"w"	    escribir (borra el contenido)
"a"	    agregar (append)
"x"	    crear (error si existe)

"r+"	leer y escribir
"w+"	(BORRA) escribir y leer
"a+"	leer + escribir (append)
"""

""" --> Trabajar en binario (img, audio, exe, etc) <--
Modo    Significado
"rb"	leer binario
"wb"	escribir binario
"ab"	agregar binario
"rb+"	leer/escribir binario
"""

with open("./Intermediate/my_file.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

# Metodos -->

contenido.read ()  # Leer todo el fichero
contenido.readline ()  # Leer una linea
contenido.readlines ()  # Leer todas las lineas (return list)

contenido.write ("Hola mundo")  # Escribir en el fichero (sobreescribe todo)
contenido.writelines ("Iterable")  # Acepta un hiterable

contenido.tell()   # posición actual del cursor
contenido.seek(0)  # mover cursos


# --------------------- Archivo JSON -------------------------

"""
json.loads (json) -> convertir de json a python
json.dumps (python) -> convertir de python a json
    -> indent=4
    -> separators = (str, str)  : cambiar los separadores
    -> sort_keys = True  : si el resultado debe ordenarse
"""
# ------------- Trabajando en local 

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
print (type (y))

# the result is a Python dictionary:
print(y["age"])

# ---------- Trabajamos con fichero.json

"""
json.load (json) -> convertir de json a python
json.dump (python) -> convertir de python a json
    -> indent=4
    -> separators = (str, str)  : cambiar los separadores
    -> sort_keys = True  : si el resultado debe ordenarse
"""

with  open (ruta_txt, "r", encoding="utf-8") as file:
    data = json.load (file)


"""
JSONDecodeError 
- e.msg → descripción humana
- e.lineno → línea donde falló
- e.colno → columna
- e.pos → posición absoluta en el archivo
"""

# NOTA: formateo decinales

# 06.2f
# ↑ ↑ ↑
# | | └─ tipo: float (f)
# | └─── precisión: 2 decimales
# └───── relleno con ceros + ancho total

# :.2f
# ↑ ↑ ↑
# | | └─ float
# | └─── 2 decimales
# └────── sin ancho, sin relleno


"""
    :< Alinea a la izquierda.
    :^ Centra el texto.
    :> Alinea a la derecha.
"""
# row[0]:02d -> Número con 2 dígitos
# row[1]:^{len_category} -> Centra el texto en un bloque de tamaño len_category

