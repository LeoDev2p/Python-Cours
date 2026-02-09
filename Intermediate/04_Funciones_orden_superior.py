
# ****  FUNCIONES DE ORDEN SUPERIOR ****

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
