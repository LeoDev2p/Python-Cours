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
