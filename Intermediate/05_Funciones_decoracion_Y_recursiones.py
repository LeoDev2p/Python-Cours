from functools import wraps

### DECORADORES : es una funcion de toma una funcion para devolver otra

# Sintaxis

def decorador(func):
    @wraps (func)    # es una buena práctica que preserva la identidad y metadatos de la función decorada, sin alterar su comportamiento.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper ()
    return wrapper

@decorador
def saludar ():
    print ("Buenos dias")

# Ejemplo .............

USUARIO = {"usuario": "cesar", "rol": "admin"}
usuario_global = {"nombre": "cesar", "rol": "admin"}

def requiere_rol(rol):
    # Este código se ejecuta al definir la función
    print(f"Decorador requiere rol '{rol}' activo")

    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Código real: validar rol antes de ejecutar la función
            if usuario_global.get("rol") != rol:
                print("❌ Acceso denegado")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorador

@requiere_rol("admin")
def eliminar_registro(id_registro):
    return f"Registro {id_registro} eliminado"

print(eliminar_registro(101))


import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()  # código antes de la función
        resultado = func(*args, **kwargs)
        fin = time.time()     # código después de la función
        print(f"⏱ Función '{func.__name__}' tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def procesar_datos(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

procesar_datos(10000)




## ----------------------------- RECURSIONES -----------------------------------

"""
Toda función recursiva debe tener dos partes:

Un caso base : una condición que detiene la recursión
Un caso recursivo : la función se llama a sí misma con un argumento modificado
"""

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))