


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
