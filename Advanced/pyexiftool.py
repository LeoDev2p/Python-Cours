# Documentación oficial: hhttps://pypi.org/project/PyExifTool/

# pip install PyExifTool

# OJO: debe tener instalado el software ExifTool en su computador

from exiftool import ExifToolHelper
from pathlib import Path
import os

BASE = Path(__file__).resolve().parent
BASE_IMG = BASE / "assets"

imagen = BASE_IMG / "foto.jpg"

with ExifToolHelper() as et:
    metadata = et.get_metadata(imagen)
    for k, v in metadata[0].items():
        print(f"{k}: {v}")


#* get_metadata() devuelve una lista de diccionarios.

metadata = et.get_metadata(imagen)

#* get_tags()
# Solo extrae etiquetas específicas
tags = et.get_tags(["foto.jpg"], tags=["EXIF:Model", "EXIF:DateTimeOriginal"])

#* set_tags() -> para escribir y editar metadatos
# Cambia el autor de la foto
et.set_tags(["foto.jpg"], tags={"EXIF:Artist": "Tu Nombre"})


#* execute() -> para ejecutar comandos personalizados de ExifTool
# Ejemplo: ejecutar un comando personalizado
et.execute("-all=", "foto.jpg")  # Esto borraría todos los metadatos


"""
OJO: ¿Cómo saber qué es editable?
La regla general es: si el dato describe 'qué es' el archivo (técnico), es solo lectura. Si describe 'quién', 'cómo' o 'dónde' se hizo la foto (descriptivo), es editable.
"""

"""
Exceptions:

exiftool.exceptions.ExifToolExecuteError:
- Intentar escribir en etiquetas de "Solo Lectura"
- El archivo no existe o la ruta está mal
- Falta de permisos en Linux
- Archivo corrupto o formato no soportado
- Sintaxis de etiquetas incorrecta

ExifToolNotFound
- ExifTool no está instalado o no se encuentra en el PATH del sistema

ExifToolStartError
- Se lanza si el programa está instalado, pero Python no logra iniciarlo (por ejemplo, por falta de memoria en el sistema o permisos de ejecución denegados).

ExifToolBufferError
- Esta es más técnica; sucede cuando la comunicación entre Python y ExifTool se rompe (el "tubo" de datos se satura o se cierra inesperadamente antes de terminar).
"""