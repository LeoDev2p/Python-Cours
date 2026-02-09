""" VARIABLES DE ENTONRO."""

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

# creamos la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

#* si el .env esta en el mismo directorio del script, no es necesario pasarle la ruta

# cargamos el archivo .env 
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

#* AUTOMATICO CON FIND_DOTENV
"""y para que python busque el .env de manera automatica, sin importar donde este el script, usamos find_dotenv() -> busca hacia arriba """

load_dotenv(find_dotenv())

SUPERUSER = os.getenv("SUPERUSER")
EMAIL = os.getenv("EMAIL")

print (SUPERUSER)


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