# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Name": "Isaias",
    "Lastname": "Errazabal",
    "Age": 23,
    "Active": False,
    "Lenguajes": {"Python", "JavaScript"}
}

my_dict = {
    "Name": "Cesar",
    "Lastname": "Quintana Errazabal",
    "Age": 23,
    "Active": False,
    "Lenguajes": {"Python", "JavaScript", "PHP", "SQL"}
}


# Búsqueda

print(my_dict[1])
print(my_dict["Name"])

print("Moure" in my_dict)
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items())  # Devuelve Clave valor en lista y tupla
print(my_dict.keys())  # Devuelve las claves en lista
print(my_dict.values())  # Devuelve los valores en lista

my_dict.update ({"Active": False})  # Actualiza / Agrega elemento al diccionario

my_dict.pop ("Active")    # Elimina los datos de la cave especificada
my_dict.popitem ()    # Elimina el ultimo elemento

my_dict.get ("Nombre")  # Devuelve el valor de la clave
my_dict.clear ()      # Limpia el diccionario


my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list), "")  # Crear un diccionario apartir de claves de un iterable, segundo argumento con lo que se va llenar el valor
print(my_new_dict)

my_dict.setdefault ("Age", 0) # Crea la clave si no esta, solo agrega valor a la clave asociada no cambia ni actualiza sus valores

# Ejemplo
d = {}
for n in [1, 2, 3, 4]:
    d.setdefault(n % 2, []).append(n)
