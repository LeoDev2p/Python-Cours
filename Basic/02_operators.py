# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### --------------- Operadores Aritméticos --------------------------- ###

# Operaciones con enteros
"""
+  --> suma
-  --> resta
* --> multiplicción
/ --> division
// --> division entera
** --> potencia
% --> modulo o resto
"""

### ------------------- Operadores de Asignación -------------------- ###
"""
=  --> asignacion sipmple
+= --> asignacion suma
-=  --> asignacion resta
+=  --> asiganacion multiplicacion
/= --> asignacion division
//=  --> asignacion division entera
**= --> asignacion potencia
%=  --> asignacion modulo
"""

"""
:= --> Asignacion morza

ejemplo:
"""
valores = [1, 2, 3, 4, 5, 6]

if (pares := [x for x in valores if x % 2 == 0]):
    print("Pares encontrados:", pares)

### ------------------- Operadores Comparativos -------------------- ###

# Operaciones con enteros
"""
>  --> mayor que
<  --> menor que
>=  --> mayor o igual que
<=  --> menor o igual que
== --> igual que
!= --> diferente que
"""

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### -------------- Operadores Lógicos---------------------- ###
"""
not --> niega un condicion
and  --> "y" (todas las condiciones deben ser verdaderas)
or --> "o" (al menos una condicion debe ser verdadero)
"""

print (4 > 2 and 3 < 5)  # True
print (4 < 2 or 3 < 5)   # True
print (not 4 > 2)        # False

### -------------- Operadores de Identidad---------------------- ###
"""  compara si dos objetos son el mismo em memoria (caja)

is --> "es igual a" (compara si dos objetos son el mismo en memoria)
is not  --> "no es igual a" (compara si dos objetos no son el mismo en memoria)
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # True
print(x is y)  # False
print(x == y)  # True

### -------------- Operadores de Menbrecia---------------------- ###
"""
in --> Devuelve True si un valor se encuentra en la secuencia
not in  --> Devuelve True si un valor no se encuentra en la secuencia
"""

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  # True
print("pineapple" not in fruits)  # True


# --------------- operadores aritmeticos de bit a bit ----------------- #

"""
~ --> not      (retorna lo opuesto -1)
& --> and      (Multiplicacion)
| --> or        (suma)
^ --> xor       (terminos iguales son 0)
<< --> desplazamiento a la izquierda
>> --> desplazamiento a la derecha
"""
## 1 byte == 8 bits --> 1    2   4   8   16  32  64  128
##                      2^0 2^1 2^2 2^3 2^4 2^5 2^6 2^7


"""
EJEMPLO

128 64 32 16 8 4 2 1
    1  0  0  0 0 0 1  -> 65
       1  0  0 0 1 0  -> 34
"""

a = 0b101
b = 0b111

# NOT bit a bit
print (~a)
print (bin (~a))  # argumento entero, devulve en bit

# AND bit a bit
print (a & b)
print (bin (a & b))

# OR bit a bit
print (a | b)
print (bin (a | b))

# XOR bit a bit
print (a ^ b)
print (bin (a ^ b))

# Desplazamiento a la derecha
print (a >> 1)
print (bin (a << 1))

# Desplzamiento a la izquierda
print (a >> 2)
print (bin (a >> 2))

"""
ASIGNACION DE BITS A BITS

&=  --> asignacion de multiplicacion de bit a bit
|=  --> asignacion de suma de bit a bit
^=  --> asignacion XOR de bit a bit
<<=  --> asignacion desplzamiento de bit a bit a la izquierda
>>=  --> asignacion desplazamiento de bit a bit a la derecha 
"""
