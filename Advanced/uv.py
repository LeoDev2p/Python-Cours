# Documentación e instalacion (window, mac, linux) uv: https://docs.astral.sh/uv/getting-started/installation/#installation-methods

#* instalacion uv en powershell

#*  ------------------------------- uv -------------------------------
"""
uv es una herramienta de gestión de proyectos y dependencias para Python, diseñada para simplificar el proceso de
la instalación de dependencias y la gestión de entornos virtuales.
"""

#* --------------------- Versiones de python --------------------------
"""
>>> uv python install    # Instalar la ultima version de python
>>> uv python install 3.12.6    # Instalar una version especifica de python
>>> uv python list    # Listar las versiones de python instaladas
>>> uv python find    # Encuentra una version de python instalada
>>> uv python pin 3.12.6    # Fija la version de python a usar en el proyecto
>>> uv python uninstall 3.12.6    # Desinstalar una version de python instalada

>>> uv python upgrade 3.12  # Actualiza a la ultima version de python disponible
"""

#* ------------------------ uv en proyectos -------------------------

#** ------------------------ Inicializacion -------------------------
"""
>>> uv init    # por defecto funciona como uv init --app, creando un proyecto con una estructura de directorios y archivos predefinidos
>>> uv init nombre-del-proyecto

>>> uv init --app   # Crea un proyecto con una estructura de directorios y archivos predefinidos, ideal para aplicaciones más complejas.
>>> uv init --lib   # Crea un proyecto con una estructura de directorios y archivos predefinidos, ideal para bibliotecas o paquetes.
>>> uv --help   # Muestra la ayuda de uv para ver todas las opciones disponibles

>>> uv add nombre-del-paquete  # Agregar una dependencia al proyecto
>>> uv remove nombre-del-proyecto  # Eliminar una dependencia del proyecto
>>> uv sync  # Sincronizar las dependencias del proyecto con el entorno

>>> uv run nombre-del-archivo.py  # Ejecuta un comando en el entorno del proyecto (si tiene dependencias)
>>> uv run    # Si el script no tiene dependencias

>>> uv tree  # Muestra la estructura de dependencias del proyecto

>>> uv lock    # Crea un archivo de bloqueo para las dependencias del proyecto

>>> uv build  # Construye el proyecto para distribución
>>> uv publish  # Publica el proyecto en un repositorio de paquetes
"""

#*  ----------------------- Utilidades ---------------------------------

"""
>>> uv cache clear    # Limpia la cache de uv
>>> uv cache prune    # Elimina paquetes de cache desactualizadas
>>> uv cache dir      # Muestra la ruta del directorio de cache uv
>>> uv tool dir      # Muestra la ruta del directorio de herramientas uv
>>> uv python dir     # Muestra la ruta del directorio de versiones de python instaladas por uv
>>> uv self update   # Actualiza uv a la ultima version disponible
"""

#* ------------------------- Herramientas de uv -------------------------
#* uvx es una herramienta para usar paquetes de python sin necesidad de instalarlos en el entorno virtual del proyecto ni en el laptop

"""
uvx paquete comando argumentos

uvx ruff checks .\main.py     =>    uv tool ruff checks .\main.py

ejem: 
    uvx ruff checks .\main.py
"""


#** Datos: uv maneja cache global, donde usa versiones de paquetes descargados y ya no los vuelve a instalarlo
