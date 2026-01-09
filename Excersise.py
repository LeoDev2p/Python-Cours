"""

🔵 NIVEL PRÁCTICO (MUY IMPORTANTE)
🔹 Lógica real

Menú con opciones (while)
1. ver carta
2. Registro de Usuario
    - superusuario
    - usuario
    - Validacion de usuario
4. carrito & Pedido
    - Valoracion por comida
6. Stadisticas
    - Usuario
    - Comidas con mas estrellas
    - Comentarios
3. Funciones de superusuario
    - Crear, eliminar, editar, y actualizar
7. Salir
"""

"""
PROGRAMAS INTERMEDIOS (muy recomendados)
5️⃣ Agenda de contactos

Guardar contactos en un diccionario
Cada contacto tiene nombre, teléfono
Agregar, buscar, eliminar
Menú de opciones

📌 Usas: dict, listas, funciones, bucles

6️⃣ Sistema de notas

Lista de alumnos
Cada alumno tiene varias notas
Calcular promedio
Mostrar aprobados y desaprobados

📌 Usas: listas, diccionarios, funciones

7️⃣ Control de inventario

Productos con nombre y cantidad
Usar diccionario
Sumar, restar stock
Validar entradas

📌 Usas: dict, bucles, funciones

8️⃣ Registro de votos

Lista de votos (nombres)
Contar votos por candidato
Mostrar ganador
Empates

📌 Usas: dict, funciones, bucles

🔵 PROGRAMAS COMPLETOS (nivel real)
9️⃣ Sistema de usuarios

Registrar usuarios
No repetir usuarios (set)
Login simple
Mostrar usuarios activos

📌 Usas: set, dict, funciones

🔟 Analizador de datos

Lista de números
Estadísticas (media, moda, frecuencia)
Mostrar resumen
Menú

📌 Usas: listas, dict, funciones

1️⃣1️⃣ Clasificador de datos

Leer datos
Clasificar por tipo
Guardar en estructuras
Reporte final

📌 Usas: listas, tuplas, sets, dict

1️⃣2️⃣ Mini sistema académico

Alumnos (nombre, notas)
Promedios
Ranking
Menú completo

📌 Usas: TODO
"""

# ----------------------------------------------------

"""
Ejericios par alambda map, filter, sorted

🧪 EJERCICIO 1 — Ranking académico
estudiantes = [
    {"nombre": "Ana", "notas": [14, 18, 17]},
    {"nombre": "Luis", "notas": [11, 12, 10]},
    {"nombre": "Carlos", "notas": [19, 18, 20]},
    {"nombre": "Maria", "notas": [15, 16, 14]}
]

🎯 Objetivo

Calcular el promedio de cada estudiante
Filtrar solo los que tienen promedio ≥ 15
Ordenarlos de mayor a menor promedio

📌 Resultado esperado: ranking por promedio (no imprimas solución)


🧪 EJERCICIO 2 — Emails válidos y ordenados por dominio
emails = [
    "ana@gmail.com",
    "luis@yahoo.com",
    "carlos@undac.edu.pe",
    "maria@hotmail.com",
    "fake@correo.xyz"
]

dominios_validos = [
    "@gmail.com",
    "@hotmail.com",
    "@undac.edu.pe"
]

🎯 Objetivo

Filtrar solo emails con dominio válid
Ordenarlos alfabéticamente por dominio
El resultado debe ser una lista


🧪 EJERCICIO 3 — Sensor IoT (datos crudos)
sensores = [
    ("T1", 22.5),
    ("T2", 40.1),
    ("T3", 18.3),
    ("T4", 35.7),
    ("T5", 12.9)
]

🎯 Objetivo

Filtrar sensores con temperatura entre 20 y 38
Transformar el valor a entero
Ordenar por temperatura descendente


🧪 EJERCICIO 4 — Sistema de ventas
ventas = [
    {"producto": "Laptop", "precio": 3500, "categoria": "tech"},
    {"producto": "Mouse", "precio": 50, "categoria": "tech"},
    {"producto": "Silla", "precio": 200, "categoria": "hogar"},
    {"producto": "Monitor", "precio": 900, "categoria": "tech"}
]

🎯 Objetivo

Filtrar solo productos de categoría "tech"
Calcular el precio con IGV (18%)
Ordenar por precio final ascendente


🧪 EJERCICIO 5 — Seguridad / passwords
passwords = [
    "Admin123",
    "root",
    "User2024",
    "123456",
    "PythonRocks"
]

🎯 Objetivo

Filtrar passwords con:
longitud ≥ 8
al menos un número
Convertirlas a minúsculas
Ordenarlas por longitud (de menor a mayor)


🧪 EJERCICIO 6 — Distancia a punto (nivel fuerte 💀)
puntos = [
    (2, 3),
    (5, 1),
    (0, 0),
    (4, 4),
    (1, 2)
]

referencia = (2, 2)

🎯 Objetivo

Calcular la distancia euclidiana de cada punto al punto referencia
Filtrar los puntos con distancia ≤ 3
Ordenarlos por distancia (del más cercano al más lejano)

📌 Usa solo map, filter, sorted, lambda
"""

# ejerciciso con generadores --------------------------------------

"""
Ejercicio 1 – Generador bidireccional (send)

Instrucción:
Crea un generador que reciba números mediante send() y devuelva el promedio acumulado hasta el momento. El generador debe detenerse cuando reciba None.

Data de ejemplo para probar:

numeros = [10, 20, 30, 5, 15]


Ejercicio 2 – Pipeline de datos con varios generadores

Instrucción:
Tienes una lista de temperaturas en Celsius. Crea un pipeline usando dos generadores encadenados con yield from:
Primer generador filtra solo las temperaturas mayores a 20°C.
Segundo generador convierte las temperaturas filtradas a Fahrenheit.

Data de ejemplo para probar:

temperaturas = [12, 25, 18, 30, 22, 15, 28]


Ejercicio 3 – Simulación de carrito multiusuario

Instrucción:
Crea un generador que simule un carrito de compras por usuario. Cada usuario envía productos al carrito (send()), y el generador devuelve el total acumulado de la compra. Al cerrar la sesión del usuario, se debe poder “terminar” el generador sin afectar a los demás usuarios.

Data de ejemplo para probar:

usuarios = {
    "Cesar": [100, 50, 25],
    "Maria": [200, 80],
    "Luis": [30, 40, 50, 20]
}
"""