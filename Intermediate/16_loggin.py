"""
Documentacion
-> https://docs.python.org/3/library/logging.html
"""
import logging
from pathlib import Path

# Usamos pathlib para crear la carpeta si no existe. 
# exist_ok=True evita que el programa falle si la carpeta ya está creada.
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

#* FORMA 1 DE CONFIGURAR ...............................
logging.basicConfig(
    # 'level' define el filtro de importancia. INFO captura INFO, WARNING, ERROR y CRITICAL.
    level=logging.INFO, 
    
    # 'format' define qué datos aparecerán en cada línea del log.
    # asctime: fecha/hora | name: nombre del logger | levelname: nivel | message: tu texto.
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    
    # 'datefmt' personaliza el formato de la fecha (Año-Mes-Día Hora:Minuto:Segundo).
    datefmt="%Y-%m-%d %H:%M:%S",
    
    # 'handlers' son los destinos de los mensajes.
    handlers=[
        # FileHandler: Guarda los mensajes en el disco.
        # encoding="utf-8": CRÍTICO para que la 'ñ' y las tildes no den error en Windows.
        logging.FileHandler("logs/app.log", encoding="utf-8"), 
        
        # StreamHandler: Muestra los mensajes en la terminal/consola en tiempo real.
        logging.StreamHandler()
    ]
)

# 3. CREACIÓN DEL OBJETO LOGGER
# Este es el objeto que importarás en tus otros archivos (Models, Controllers).
# El nombre "AppGestion" aparecerá en la columna %(name)s de tus logs.
logger = logging.getLogger("AppGestion")

# Ejemplo de uso:
logger.info("El sistema de logging se ha iniciado correctamente.")


#* FORMA 2 DE CONFIGURAR  RECOMENDABLE..............................................

def get_logger(name):
    logger = logging.getLogger(name)
    
    # Importante: Si el logger ya tiene handlers, no agregues más
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Formato común
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Handler de Archivo
        file_h = logging.FileHandler("Logs/app.log", encoding='utf-8')
        file_h.setFormatter(formatter)
        
        # Handler de Consola
        stream_h = logging.StreamHandler()
        stream_h.setFormatter(formatter) # <-- Corregido aquí

        logger.addHandler(file_h)
        logger.addHandler(stream_h)
        
        # Evita que el mensaje suba al logger raíz y se duplique
        logger.propagate = False 
        
    return logger


# Algunos de los formateadores
"""
Nombre del atributo     Formato         Descripción

asctime                 %(asctime)s     Tiene el formato '2003-07-08 16:49:45,896' (los números después de la coma corresponden a la fracción de milisegundos).
creado                  %(created)f     Hora en que LogRecordse creó (según lo devuelto por time.time_ns()/ 1e9).
Nombre del archivo      %(filename)s    Parte del nombre del archivo pathname.
nombreFunción           %(funcName)s    Nombre de la función que contiene la llamada de registro.
nombre de nivel         %(levelname)s   Nivel de registro de texto para el mensaje ( 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
nivel no                %(levelno)s     Nivel de registro numérico para el mensaje ( DEBUG, INFO, WARNING, ERROR, CRITICAL).
lino                    %(lineno)d      Número de línea de origen donde se emitió la llamada de registro (si está disponible).
mensaje                 %(message)s     El mensaje registrado, calculado como . Se establece cuando se invoca.msg % argsFormatter.format()
módulo                  %(module)s      Módulo (parte del nombre filename).
nombre                  %(name)s        Nombre del registrador utilizado para registrar la llamada.
"""