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

from functools import wraps

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


### ------------- funcinoes Lambda -----------------------

"""
Sintaxis

lambda arguments : expression

--> Utilice funciones lambda cuando se requiera una función anónima por un corto período de tiempo.
"""

x = lambda a : a + 10
print(x(5))

es_mayor = lambda edad: "Mayor" if edad >= 18 else "Menor"
print(es_mayor(20))

sum_total = lambda x: sum((k for k in range (x) if k % 2 == 0))
print (sum_total)

# lambda como funcion anonima dentro de una funcion

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# **** Lambda con funciones ****

"""
map ()  -> aplica una función a cada elemento de un iterable y devuelve los resultados.

map(función, iterable)
"""

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(list(doubled))


"""
mafilter ()  -> selecciona elementos según una condición

filter(función, iterable)
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

"""
sorted ()  -> Orden personalizado

sorted(iterable, key=funcion)

🟢 Si necesitas criterio personalizado → key
🟢 Si necesitas orden inverso → reverse=True
"""

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


"""
reduce ()  -> un iterable a un solo valor, acumulando resultados. (siempre espera 2 parametros)

reduce(funcion, iterable, valor_inicial_opcional)

-> funcion: recibe 2 parámetros
-> iterable: lista, tupla, etc.
-> valor_inicial: opcional
"""

from functools import reduce

nums = [1, 2, 3, 4]

resultado = reduce(lambda a, b: a + b, nums)
print(resultado)


palabras = ["Hola", "mundo", "Python"]
resultado = reduce(lambda a, b: a + " " + b, palabras)
print (resultado)

## *************** FUNCIONES EXTRAS ****************

"""
any () --> devuelve True si AL MENOS UN ELEMENTO del iterable es verdadero.
any (iterable)
"""

any([0, False, "", 5])  # True

numeros = [1, 3, 5, 8]
any(x % 2 == 0 for x in numeros)  # True


"""
all () devuelve True SOLO SI TODOS los elementos son verdaderos.
all (iterable) 
"""

all([1, True, "hola"]) # True
all([1, 0, 3])  # False

numeros = [2, 4, 6, 8]
all(x % 2 == 0 for x in numeros)  # True


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


## -----------------------GENERADORES -----------------------------------

"""
Es una función que: Produce valores uno por uno ; No guarda todo en memoria; Se pausa y continúa ; Se crean con yield & yield from.
"""

# ejemplo 1
def generator ():
    for k in range (10):
        yield k

result = generator ()
print (next (result))  # 0
print (next (result))  # 1

# ejemplo 2
data = (x for x in range (10))

# ejemplo 3
lista = ["@email.com", "@hotmail.com", "@edu.pe.com"]

def generador ():
    yield from lista  # funciona como un for

var = generador ()
print (next (var)) # @gmail.com
print (next (var)) # @hotmail.com

# funcion send "Comunicacion bidireccional"

def acumulador():
    total = 0
    while True:
        valor = yield total  # yield devuelve total
        total += valor 


gen = acumulador()
print(next(gen))    # arranca el generador, imprime 0
print(gen.send(5))  # envía 5, imprime 5
print(gen.send(3))  # envía 3, imprime 8



# ************** funcion iter () ******************

"""
iterador : lo que se consume de uno a uno
iterable: lo que se puede recorrer, list, dict, set, tuple, range
"""

lista = [1, 2, 3, 4, 5]
var = iter (lista)

print (next (var)) # 1
print (next (var)) # 2
