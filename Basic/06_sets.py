# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###  --> es una colección desordenada , inmutable* y no indexada .

# Definición

my_set1 = set()
my_set = {}

print(type(my_set1))
print(type(my_set))  # Inicialmente es un diccionario


my_set = {"Cesar", "Quintana", 23}
my_set1 = {"Mia", "Armas", 21, "Cesar"}
print(type(my_set))

print(len(my_set))
my_set.add("Isaias")            # Permite agregar un elemento al conjunto
my_set.update ([1, 2, 3, 4])    # Permite agregar un iterable

my_set.remove ("Cesar")   # Elimina el elemento del conjunto (si no esta da error)
my_set.discard ("Quintana")  # Elimina el elemento del conjunto  (No nada error)
my_set.pop ()           # Elimina un valor aleatorio (devuelve el valor eliminado)
my_set.clear()          # Limpia el conjunto completo
my_set.copy ()          # Copia los datos en un nuevo conjunto
# del my_set     # con del se elimina la caja en memoria

my_set.union (my_set1, {"Yolanda", "Errazabal", 53})  # Devuelve un nuevo conjunto o  "|" en ves del metodo
my_set.intersection (my_set1)  # Devuelve un nuevo conjunto solo con datos iguales o "&" en ves del metodo
my_set.intersection_update (my_set1)  # Modifica el conjunto 1
my_set.difference (my_set1)  # Devuelve nuevo conjunto conservando todos los elementos del conjunto 1 que no estén en el conjunto 2  o usar "-" en ves del metodo
my_set.difference_update (my_set1)  # Modifica en el conjunto 1
my_set.symmetric_difference (my_set1)  # conservará únicamente los elementos que NO estén presentes en ambos conjuntos. o usar "^"
my_set.symmetric_difference_update (my_set1) # Modifica el conjunto 1

### Frozenset  ###     Version inmutable del set

"""
copy ()
union ()
difference ()
intersection ()
symetric_difference ()

issubset ()   -> Devulve True si todos los elementos del set1 están dentro del set2
issuperset () -> Devuelve True si todos set1 tiene todos los elementos del set2 
isdisjoint ()  -> Devuelve true si  no comparten elementos entre set
"""

new = frozenset ({1,2})
new1 = frozenset ({3, 4, 5, 6})

print (new.issubset (new1))

print (new1.issuperset (new))
print (new.isdisjoint (new1))