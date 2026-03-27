
### Functions ###

# Definición

def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()

# global    --> Para especificar que una variable es global

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values("5", "7")

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="LeoDev", name="Black")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("LeoDev", "Black")
print_name_with_default("LeoDev", "Black", "LeoDev2p")

# Función con parámetros de entrada/argumentos arbitrarios

# *args  ->  si no sabe cuantos argumentos pasara (lo toma como tupla)
# **kwargs  -> si no sabe cuantos argumentos clave valor pasara (lo toma como diccinoario)

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "LeoDev")
print_upper_texts("Hola")


#* OJO: 
#* Empqueta *args **kwargs cuando se define en la funcion uqe se crea
#* Desempaqueta *args **kwargs cuando se define en la llamada de la funcion creada

"""
def numero (*args): -> empaquetamos
... print(args)


num = (1, 2, 3, 4, 5)
numero(*num) -> Desempaquetamos
"""