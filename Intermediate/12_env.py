""" VARIABLES DE ENTONRO."""

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv, dotenv_values

# creamos la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

#* si el .env esta en el mismo directorio del script, no es necesario pasarle la ruta

# cargamos el archivo .env  primero y luego del sistema
load_dotenv()

# obtenemos el valor de la variable de entorno SUPERUSER
SUPERUSER = os.getenv("SUPERUSER")
EMAIL = os.getenv("EMAIL")

print (SUPERUSER)


#* MANUAL CON PATHLIB

"""si esta en el .env esta en otro directorio del script, pasamos la ruta al cargar el .env -> busca solo en esa carpeta"""

    # Cargamos el archivo .env desde la ruta especificada
load_dotenv(BASE_DIR / ".env")

SUPERUSER = os.getenv("SUPERUSER")
EMAIL = os.getenv("EMAIL")

print (SUPERUSER)


#* CARGAR VARIABLES DE ENTORNO SOLO DE MI .env

    # no se mezcla con las variables de entorno del sistema operativo, solo carga lo que esta en el .env como diccionario
config = dotenv_values(".env")
print(config) # Esto devuelve solo lo que está en tu archivo .env

#* AUTOMATICO CON FIND_DOTENV
"""y para que python busque el .env de manera automatica, sin importar donde este el script, usamos find_dotenv() -> busca hacia arriba """

# override=True hace que el .env mande sobre el sistema
load_dotenv(find_dotenv(), override=True)

SUPERUSER = os.getenv("SUPERUSER")
EMAIL = os.getenv("EMAIL")

print (SUPERUSER)


# CARGAR VARIABLES DE ENTORNO DESDE EL SISTEMA OPERATIVO

enviroment = dict(os.environ) # con dict para verlo como diccionario, sino se ve como un objeto de tipo os._Environ
print(enviroment)

"""
SISTEMA_GESTION/ (Raíz)
├── .env  <------------------- 🏁 ¡ENCONTRADO! (Aquí se detiene)
│
├── app/  <------------------- 🔍 2° Intento: Busca aquí... (No está)
│   ├── core/  <-------------- 🔍 1° Intento: Busca aquí... (No está)
│   │   └── config.py  <------ 🚀 INICIO: Ejecutas load_dotenv(find_dotenv())
│   ├── controllers/
│   ├── models/
│   └── views/
│
├── data/
└── logs/

"""

NOTA = "Tener en cuenta lo siguiente"
"""
Si el valor de tu variable tiene espacios o símbolos especiales (como #, @, !), usa siempre comillas dobles " ".
"""